#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def getsize(s):
    return len(s) - len([x for x in s if x == "\\"])


INIT = 100
MAX_DIGIT = 16


def first1000():
    output = []
    for i in range(1, INIT):
        if i % 15 == 0:
            output.append('FizzBuzz\\n')
        elif i % 3 == 0:
            output.append('Fizz\\n')
        elif i % 5 == 0:
            output.append('Buzz\\n')
        else:
            output.append('%d\\n' % i)
    return 'const char* GEN_FIRST_1000 = "' + ''.join(output) + '";'


def geninsts(head, digit):
    fmt = '%02d\\n'
    buf = ''
    sizes = []
    bc, dc = 0, 0
    head *= INIT
    insts = []
    for i in range(0, INIT):
        if (head + i) % 15 == 0:
            buf += 'FizzBuzz\\n'
        elif (head + i) % 3 == 0:
            buf += 'Fizz\\n'
        elif (head + i) % 5 == 0:
            buf += 'Buzz\\n'
        else:
            if buf:
                sizes.append(getsize(buf))
                insts.append((buf, sizes[-1]))
                bc += sizes[-1]
                buf = ''
            insts.append(('pp', digit))
            dc += 1
            s = fmt % i
            buf += s
    if buf:
        sizes.append(getsize(buf))
        insts.append((buf, sizes[-1]))
        bc += sizes[-1]
    return insts, sizes, bc, dc


def gencode(head, digit):
    insts, _, _, _ = geninsts(head, digit)
    output = ['char* gen_output_%s_%s(char* RE buf, const char* RE pp) {' % (head, digit)]
    for p, size in insts:
        if p == 'pp':
            output.append('MC(pp, %d);' % (size))
        else:
            output.append('MC("%s", %d);' % (p, size))
    output.append('return buf;\n}')
    return output


def makevalue(s, off, size):
    s = s.replace('\\n', "\n")
    seq = []
    val = 0
    for i in range(off, off + size):
        seq.append(ord(s[i]))
    for _ in range(32 - len(seq)):
        seq.append(0)

    e0, e1, e2, e3 = 0, 0, 0, 0
    for i in reversed(range(8)):
        e3 = e3 * 256 + seq[i + 24]
        e2 = e2 * 256 + seq[i + 16]
        e1 = e1 * 256 + seq[i + 8]
        e0 = e0 * 256 + seq[i]
    return e3, e2, e1, e0


def gencode256(head, digit):
    insts, _, _, _ = geninsts(head, digit)
    O = ['char* gen_output_%s_%s(char* RE buf, const char* RE pp) {' % (head, digit)]
    MODE = 256
    INIT = MODE // 8
    cap = INIT

    O.append('uint64_t e0=0,e1=0,e2=0,e3=0;')
    sz = digit
    off = 0
    for i in range(4):
        if sz == 0: break
        load = min(sz, 8)
        O.append('memcpy(&e%d, pp + %d, %d);' % (i, off, load))
        off += 8
        sz -= load

    O.append('__m256i PP = _mm256_set_epi64x(e3, e2, e1, e0);')
    O.append('__m256i X = _mm256_setzero_si256();')
    O.append('__m256i P, C;')

    def mm256_merge(x, y, off, size):
        assert size <= 16
        if off == 0:
            return "%s = %s;" % (x, y)

        if off + size <= 16:
            return "%s = _mm256_or_si256(%s, _mm256_bslli_epi128(%s, %s));" % (x, x, y, off)

        # FIXME: not efficient.
        rshift = 16 - off
        if rshift > 0:
            inst = "__m256i t3 = _mm256_bsrli_epi128(t2, %d);" % (rshift);
        elif rshift < 0:
            inst = "__m256i t3 = _mm256_bslli_epi128(t2, %d);" % (-rshift);
        else:
            inst = "__m256i t3 = t2;"

        C = """{{ // mm256_merge({target}, {source}, {shift}, {size});
__m256i t = _mm256_bslli_epi128({source}, {shift});
__m256i t2 = _mm256_permute2f128_si256({source}, {source}, 0x08);
{inst}
{target} = _mm256_or_si256({target}, _mm256_or_si256(t, t3));
}}
""".format(target=x, source=y, shift=off, size=size, rshift=16 - off, inst=inst)
        return C

    def mm256_rshift(x, y, off, size):
        if off == 0:
            return "%s = %s;" % (x, y)
        assert size <= 16
        # size <= 16, so there is no cross-lane operations.
        # return '// %s = mm256_rshift(%s, %s, %s);' % (x, y, off, size);
        return '%s = _mm256_bsrli_epi128(%s, %s); ' % (x, y, off)

    def loadP(off):
        C = mm256_rshift("P", "PP", off, digit)
        O.append(C)

    def mergeP(cap, load):
        off = INIT - cap
        C = mm256_merge("X", "P", off, load)
        O.append(C)

    def flushX(cap, force=False):
        if (cap == 0 or force) and (INIT - cap) != 0:
            C = "_mm256_storeu_si256((__m256i*)buf, X); /* X = _mm256_setzero_si256(); */ buf += %d;" % (INIT - cap)
            O.append(C)
            cap = INIT
        return cap

    def makeC(e3, e2, e1, e0, p):
        C = 'C = _mm256_set_epi64x(%dLL, %dLL, %dLL, %dLL); // %s' % (e3, e2, e1, e0, p)
        O.append(C)

    def shiftC(off):
        if off > 0:
            # C does not cross 128-bit lane.
            C = "C = _mm256_bsrli_epi128(C, %d);" % (off)
            O.append(C)

    def mergeC(cap, load):
        off = INIT - cap
        C = mm256_merge("X", "C", off, load)
        O.append(C)

    for p, size in insts:
        if p == 'pp':
            off = 0
            while size:
                load = min(cap, size)
                loadP(off)
                mergeP(cap, load)

                cap -= load
                size -= load
                off += load

                cap = flushX(cap)
        else:
            assert size <= 16
            off = 0
            e3, e2, e1, e0 = makevalue(p, 0, size)
            makeC(e3, e2, e1, e0, p)
            while size:
                load = min(cap, size)
                shiftC(off)
                mergeC(cap, load)
                cap -= load
                size -= load
                off = load

                cap = flushX(cap)

    cap = flushX(cap, True)
    O.append('return buf;\n}')
    return O


def gencode128(head, digit):
    insts, _, _, _ = geninsts(head, digit)
    O = ['char* gen_output_%s_%s(char* RE buf, const char* RE pp) {' % (head, digit)]
    MODE = 128
    INIT = MODE // 8
    cap = INIT

    class Context:
        def __init__(self):
            self.inst = 0
            self.store = 0

        def inc_inst(self, v):
            self.inst += v

        def inc_store(self):
            self.store += 1

    ctx = Context()

    O.append('uint64_t e0=0,e1=0;')
    sz = digit
    off = 0
    for i in range(2):
        if sz == 0: break
        load = min(sz, 8)
        O.append('memcpy(&e%d, pp + %d, %d);' % (i, off, load))
        off += 8
        sz -= load

    O.append('__m128i PP = _mm_set_epi64x(e1, e0);')
    O.append('__m128i X = _mm_setzero_si128();')
    O.append('__m128i P, C;')

    def mm128_merge(x, y, off):
        if off == 0: return "%s = %s;" % (x, y)
        ctx.inc_inst(2)
        return "%s = _mm_or_si128(%s, _mm_bslli_si128(%s, %s));" % (x, x, y, off)

    def flushX(cap, force=False):
        if (cap == 0 or force) and (INIT - cap) != 0:
            C = "_mm_storeu_si128((__m128i*)buf, X); /* X = _mm_setzero_si128(); */ buf += %d;" % (INIT - cap)
            ctx.inc_store()
            O.append(C)
            cap = INIT
        return cap

    # there is no P variable.
    reduceLoadP = False
    if reduceLoadP:
        def loadP(off):
            pass

        def mergeP(off, cap):
            if cap == INIT:
                if off == 0:
                    C = "X = PP;"
                else:
                    ctx.inc_inst(1)
                    C = "X = _mm_bsrli_si128(PP, %d);" % (off)
            else:
                if off == 0:
                    ctx.inc_inst(2)
                    C = "X = _mm_or_si128(X, _mm_bslli_si128(PP, %d));" % (INIT - cap)
                else:
                    ctx.inc_inst(3)
                    C = "X = _mm_or_si128(X, _mm_bslli_si128(_mm_bsrli_si128(PP, %d), %d));" % (off, INIT - cap)
            O.append(C)
    else:
        def mm128_rshift(x, y, off):
            if off == 0: return "%s = %s;" % (x, y)
            ctx.inc_inst(1)
            return "%s = _mm_bsrli_si128(%s, %d);" % (x, y, off)

        def loadP(off):
            C = mm128_rshift("P", "PP", off)
            O.append(C)

        def mergeP(off, cap):
            C = mm128_merge("X", "P", INIT - cap)
            O.append(C)

    # there is no C variable.
    reduceLoadC = False
    if not reduceLoadC:
        def makeC(e3, e2, e1, e0, p):
            C = 'C = _mm_set_epi64x(%dLL, %dLL); // %s' % (e1, e0, p)
            O.append(C)

        def shiftC(off):
            if off > 0:
                ctx.inc_inst(1)
                C = "C = _mm_bsrli_si128(C, %d);" % (off)
                O.append(C)

        def mergeC(cap, load):
            off = INIT - cap
            C = mm128_merge("X", "C", off)
            O.append(C)

    for p, size in insts:
        if p == 'pp':
            off = 0
            while size:
                load = min(cap, size)
                loadP(off)
                mergeP(off, cap)

                cap -= load
                size -= load
                off += load

                cap = flushX(cap)
        else:
            assert size <= 16
            off = 0
            e3, e2, e1, e0 = makevalue(p, 0, size)
            assert (e3, e2) == (0, 0)
            if not reduceLoadC:
                makeC(e3, e2, e1, e0, p)
            while size:
                load = min(cap, size)
                if not reduceLoadC:
                    shiftC(off)
                    mergeC(cap, load)
                    off = load
                else:
                    # we shift constant value right here.
                    mask = (1 << 128) - 1
                    tmp = (e1 << 64) | (e0)
                    tmp = (tmp >> (off * 8)) & mask
                    tmp = (tmp << ((INIT - cap) * 8)) & mask
                    mask = (1 << 64) - 1
                    t1, t0 = (tmp >> 64) & mask, tmp & mask
                    if cap == INIT:
                        C = "X = _mm_set_epi64x(%dLL, %dLL);" % (t1, t0)
                    else:
                        ctx.inc_inst(1)
                        C = "X = _mm_or_si128(X, _mm_set_epi64x(%dLL, %dLL));" % (t1, t0)
                    C += "// (%s >> %d) << %d" % (p, off, INIT - cap)
                    O.append(C)
                    off += load

                cap -= load
                size -= load
                cap = flushX(cap)

    cap = flushX(cap, True)
    O.append('// insts = %d, stores = %d, stores/insts = %.2f' % (ctx.inst, ctx.store, ctx.store / ctx.inst))
    O.append('return buf;\n}')
    return O


def gencode128v2(head, digit):
    insts, _, _, _ = geninsts(head, digit)
    O = ['char* gen_output_%s_%s(char* RE buf, const char* RE pp) {' % (head, digit)]
    MODE = 128
    INIT = MODE // 8
    cap = INIT
    unroll = 2

    class Context:
        def __init__(self):
            self.inst = 0
            self.store = 0
            self.used = 0
            self.bp = 0

        def inc_inst(self, v):
            self.inst += v

        def inc_store(self):
            self.store += 1

        def getX(self):
            return "X%d" % (self.used)

        def nextX(self):
            self.used = (self.used + 1) % unroll

    ctx = Context()

    O.append('uint64_t e0=0,e1=0;')
    sz = digit
    off = 0
    for i in range(2):
        if sz == 0: break
        load = min(sz, 8)
        O.append('memcpy(&e%d, pp + %d, %d);' % (i, off, load))
        off += 8
        sz -= load

    O.append('__m128i PP = _mm_set_epi64x(e1, e0);')
    for i in range(unroll):
        O.append('__m128i X%d = _mm_setzero_si128();' % (i))

    def flushX(cap, force=False):
        if (cap == 0 or force) and (INIT - cap) != 0:
            ctx.inc_store()
            C = "_mm_storeu_si128((__m128i*)(buf + %d), %s);" % (ctx.bp, ctx.getX())
            ctx.bp += (INIT - cap)
            ctx.nextX()
            O.append(C)
            cap = INIT
        return cap

    def mergeP(off, cap):
        if cap == INIT:
            if off == 0:
                C = "%s = PP;" % (ctx.getX())
            else:
                ctx.inc_inst(1)
                C = "%s = _mm_bsrli_si128(PP, %d);" % (ctx.getX(), off)
        else:
            if off == 0:
                ctx.inc_inst(2)
                X = ctx.getX()
                C = "%s = _mm_or_si128(%s, _mm_bslli_si128(PP, %d));" % (X, X, INIT - cap)
            else:
                ctx.inc_inst(3)
                X = ctx.getX()
                C = "%s = _mm_or_si128(%s, _mm_bslli_si128(_mm_bsrli_si128(PP, %d), %d));" % (
                    X, X, off, INIT - cap)
        O.append(C)

    for p, size in insts:
        if p == 'pp':
            off = 0
            while size:
                load = min(cap, size)
                mergeP(off, cap)

                cap -= load
                size -= load
                off += load

                cap = flushX(cap)
        else:
            assert size <= 16
            off = 0
            e3, e2, e1, e0 = makevalue(p, 0, size)
            assert (e3, e2) == (0, 0)
            while size:
                load = min(cap, size)
                # we shift constant value right here.
                mask = (1 << 128) - 1
                tmp = (e1 << 64) | (e0)
                tmp = (tmp >> (off * 8)) & mask
                tmp = (tmp << ((INIT - cap) * 8)) & mask
                mask = (1 << 64) - 1
                t1, t0 = (tmp >> 64) & mask, tmp & mask
                if cap == INIT:
                    C = "%s = _mm_set_epi64x(%dLL, %dLL);" % (ctx.getX(), t1, t0)
                else:
                    ctx.inc_inst(1)
                    X = ctx.getX()
                    C = "%s = _mm_or_si128(%s, _mm_set_epi64x(%dLL, %dLL));" % (X, X, t1, t0)
                C += " // (%s >> %d) << %d" % (p, off, INIT - cap)
                O.append(C)
                off += load

                cap -= load
                size -= load
                cap = flushX(cap)

    cap = flushX(cap, True)
    O.append('// insts = %d, stores = %d, stores/insts = %.2f' % (ctx.inst, ctx.store, ctx.store / ctx.inst))
    O.append('return buf + %d;\n}' % (ctx.bp))
    return O


# gencode = gencode256
# gencode = gencode128
gencode = gencode128v2

with open('fizzbuzz-gen.h', 'w') as fh:
    _, ss1, a1, b1 = geninsts(1, 1)
    _, ss2, a2, b2 = geninsts(2, 1)
    _, ss3, a3, b3 = geninsts(3, 1)
    ss = list(set(ss1 + ss2 + ss3))
    ss.sort()
    print('memory copy object size = <digit> + ', ss)

    fh.write("""#define GEN_COMPUTE_SIZE \\
int size0 = %d + d0 * %d; \\
int size1 = %d + d1 * %d + size0; \\
int size2 = %d + d2 * %d + size1;
constexpr int GEN_INIT = %d;
constexpr int GEN_STEP = %d;
""" % (a1, b1, a2, b2, a3, b3, INIT, INIT * 3))
    fh.write(first1000())
    fh.write('\n')

    for digit in range(1, MAX_DIGIT + 1):
        output1 = gencode(1, digit)
        output2 = gencode(2, digit)
        output3 = gencode(3, digit)
        for s in output1 + output2 + output3:
            fh.write(s + '\n')

    for x in (1, 2, 3):
        fh.write("char* GEN_OUTPUT_%s(char* buf, const char* p, int digit) {\n" % (x))
        fh.write("switch(digit) {\n")
        for digit in range(1, MAX_DIGIT + 1):
            fh.write("case %d: return gen_output_%s_%s(buf, p);\n" % (digit, x, digit))
        fh.write("default: return nullptr;\n")
        fh.write("}\n}\n")

if __name__ == '__main__':
    pass
