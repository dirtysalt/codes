#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

import unittest


def zigzag(x):
    return (x << 1) ^ (x >> 63)


def unzigzag(x):
    return (x >> 1) ^ (-(x & 1))


def _encode_varint(x, bs):
    while x >= 128:
        bs.append(128 | (x & 0x7f))
        x = x >> 7
    bs.append(x & 0x7f)


def encode_varint(x):
    bs = []
    _encode_varint(x, bs)
    return bytes(bs)


def _decode_varint(bs, off=0):
    i = off
    x = 0
    shift = 0
    while i < len(bs):
        x = x | ((bs[i] & 0x7f) << shift)
        if bs[i] < 128:
            i += 1
            break
        i += 1
        shift += 7
    return x, i


def decode_varint(bs):
    value, _ = _decode_varint(bs)
    return value


def widthInBits(value):
    if value == 0: return 1
    ans = 0
    while value:
        value = value >> 1
        ans += 1
    return ans


def widthInBytes(value):
    bits = widthInBits(value)
    return (bits + 7) // 8


class OutputByteStream:
    def __init__(self):
        self.buf = []

    def append(self, value):
        self.buf.append(value)

    def extend(self, values):
        self.buf.extend(values)

    def asBytes(self):
        return bytes(self.buf)

    def encodeVarint(self, value):
        _encode_varint(value, self.buf)

    def writeInt(self, value, w):
        for i in reversed(range(w)):
            self.buf.append((value >> (i * 8)) & 0xff)

    def clear(self):
        self.buf.clear()


class InputByteStream:
    def __init__(self, bs):
        self.bs = bs
        self.pos = 0
        self.size = len(bs)

    def read(self, n=1, single=True):
        self.pos += n
        ret = self.bs[self.pos - n: self.pos]
        if n == 1 and single:
            return ret[0]
        return ret

    def backup(self, n=1):
        self.pos -= n

    def empty(self):
        return self.pos == self.size

    def decodeVarint(self):
        ret, end = _decode_varint(self.bs, self.pos)
        self.pos = end
        return ret

    def readInt(self, w):
        value = 0
        for i in range(w):
            value = (value << 8) | self.bs[self.pos + i]
        self.pos += w
        return value


# ==================== RLEv1 ==========

class ByteRLE:
    def __init__(self, leastRepeat=3):
        self.maxsize = 128
        self.leastRepeat = leastRepeat
        self.buf = [None] * self.maxsize
        self.bs = OutputByteStream()
        self.pos = 0
        self.tail = 0
        self.repeat = False

    def add(self, x):
        self.buf[self.pos] = x
        self.pos += 1

        if self.pos >= self.maxsize:
            self._flush(self.pos)
            self.pos = 0
            return

        p = self.pos
        if p >= 2:
            if self.buf[p - 1] == self.buf[p - 2]:
                self.tail += 1
                if self.tail == self.leastRepeat:
                    assert (self.repeat == False)
                    self._flush(p - self.leastRepeat)
                    self.repeat = True
                    self.buf[0] = self.buf[p - 1]
                    self.pos = 1

            else:
                if self.tail >= self.leastRepeat:
                    assert (self.repeat == True)
                    self._flush(p - 1)
                    self.buf[0] = self.buf[p - 1]
                    self.pos = 1
                    self.repeat = False
                self.tail = 1
        else:
            self.tail = 1
            self.repeat = False

    def flush(self):
        self._flush(self.pos)
        self.pos = 0
        self.tail = 0
        self.repeat = False

    def _flush(self, p):
        if p <= 0:
            return
        if self.repeat:
            assert (self.tail >= self.leastRepeat)
            self.encodeRepeat(self.tail, self.buf[0])
        else:
            self.encodeNonRepeat(p, self.buf[:p])

    def encodeNonRepeat(self, size, buf):
        assert size <= 128 and size >= 1
        self.bs.extend([(-size) & 0xff] + buf)

    def encodeRepeat(self, number, value):
        self.bs.extend([number - 3, value])

    def getBytes(self):
        return self.bs.asBytes()

    def reset(self):
        self.bs.clear()
        self.pos = 0
        self.tail = 0
        self.repeat = False

    def addMany(self, buf):
        for x in buf:
            self.add(x)


class ByteRLEDecoder:
    def __init__(self):
        pass

    def decode(self, bs):
        if isinstance(bs, bytes):
            bs = InputByteStream(bs)
        buf = []
        while not bs.empty():
            b = bs.read()
            if b >= 128:
                b = ~(b - 1) & 0xff
                buf.extend(bs.read(b, single=False))
            else:
                b += 3
                buf.extend([bs.read()] * b)
        return buf


class BitRLEDecoder(ByteRLEDecoder):
    def __init__(self):
        parent = super(BitRLEDecoder, self)
        parent.__init__()
        self.parent = parent

    def decode(self, bs, bits):
        buf = self.parent.decode(bs)
        buf2 = []
        for b in buf:
            for i in reversed(range(8)):
                buf2.append((b >> i) & 0x1)
        buf2 = buf2[:bits]
        return buf2


class BitRLE(ByteRLE):
    def __init__(self, leastRepeat):
        parent = super(BitRLE, self)
        parent.__init__(leastRepeat)
        self.parent = parent
        self.lastByte = 0
        self.lastRemaing = 8

    def add(self, b):
        self.lastByte |= ((b & 0x1) << (self.lastRemaing - 1))
        self.lastRemaing -= 1
        if self.lastRemaing == 0:
            self.parent.add(self.lastByte)
            self.lastByte = 0
            self.lastRemaing = 8

    def flush(self):
        if self.lastRemaing != 8:
            self.add(self.lastByte)
            self.lastRemaing = 8
            self.lastByte = 0
        self.parent.flush()


class RLEv1:
    def __init__(self, leastRepeat=3):
        self.maxsize = 128
        self.leastRepeat = leastRepeat
        self.buf = [None] * self.maxsize
        self.bs = OutputByteStream()
        self.pos = 0
        self.tail = 0
        self.repeat = False
        self.delta = None
        self.base = None

    def add(self, x):
        self.buf[self.pos] = x
        self.pos += 1

        if self.pos >= self.maxsize:
            self._flush(self.pos)
            self.pos = 0
            return

        p = self.pos
        if p >= 2:
            if self.delta is not None and (self.buf[p - 2] + self.delta) == self.buf[p - 1]:
                self.tail += 1
                if self.tail == self.leastRepeat:
                    assert (self.repeat == False)
                    self._flush(p - self.leastRepeat)
                    self.repeat = True
                    self.base = self.buf[p - self.leastRepeat]
                    self.buf[0] = self.buf[p - 1]
                    self.pos = 1

            else:
                if self.tail >= self.leastRepeat:
                    assert (self.repeat == True)
                    self._flush(p - 1)
                    self.buf[0] = self.buf[p - 1]
                    self.pos = 1
                    self.repeat = False
                    self.tail = 1
                    self.delta = None
                else:
                    new_delta = self.buf[p - 1] - self.buf[p - 2]
                    if -128 <= new_delta <= 127:
                        self.delta = new_delta
                        self.tail = 2
                    else:
                        self.delta = None
                        self.tail = 1
        else:
            self.delta = None
            self.tail = 1
            self.repeat = False

    def flush(self):
        self._flush(self.pos)
        self.pos = 0
        self.tail = 0
        self.repeat = False
        self.delta = None

    def _flush(self, p):
        if p <= 0:
            return
        if self.repeat:
            assert (self.tail >= self.leastRepeat)
            self.encodeRepeat(self.tail, self.base, self.delta)
        else:
            self.encodeNonRepeat(p, self.buf[:p])

    def encodeNonRepeat(self, size, values):
        assert size <= 128 and size >= 1
        self.bs.append((-size) & 0xff)
        for x in values:
            _encode_varint(x, self.bs)

    def encodeRepeat(self, number, value, delta):
        # print(number, value, delta)
        self.bs.append(number - 3)
        self.bs.append(delta & 0xff)
        _encode_varint(value, self.bs)

    def getBytes(self):
        return self.bs.asBytes()

    def reset(self):
        self.bs.clear()
        self.pos = 0
        self.tail = 0
        self.repeat = False
        self.delta = None

    def addMany(self, buf):
        for x in buf:
            self.add(x)


class StringEncoder:
    def __init__(self):
        # string -> index
        self.dict = {}
        self.count = 0
        self.refs = []

    def add(self, s):
        self.count += 1
        if s not in self.dict:
            ref = len(self.dict)
            self.dict[s] = ref
        else:
            ref = self.dict[s]
        self.refs.append(ref)

    def addMany(self, ss):
        for s in ss:
            self.add(s)

    def reset(self):
        self.dict.clear()
        self.count = 0
        self.refs.clear()

    def encodeDirect(self):
        # !!! make reverse dict.
        rev = [None] * len(self.dict)
        for k, index in self.dict.items():
            rev[index] = k

        data = ''.join([rev[x] for x in self.refs])
        length = [len(rev[x]) for x in self.refs]
        return data, length

    def encodeDictionary(self):
        # !!! use c++ ordered map
        keys = sorted(self.dict.keys())
        rev = [None] * len(self.dict)
        for i in range(len(keys)):
            index = self.dict[keys[i]]
            rev[index] = i

        ddata = ''.join(keys)
        length = [len(x) for x in keys]
        data = [rev[x] for x in self.refs]
        return ddata, length, data


class StringDecoder:
    def __init__(self):
        pass

    def decodeDirect(self, data, length):
        ans = []
        p = 0
        for x in length:
            ans.append(data[p:p + x])
            p += x
        return ans

    def decodeDictinary(self, ddata, length, data):
        ans = []
        p = 0
        for x in length:
            ans.append(ddata[p:p + x])
            p += x
        res = []
        for index in data:
            res.append(ans[index])
        return res


# ==================== RLEv2 ====================

class Options:
    def __init__(self):
        self.signed = False
        self.aligned = False


_defaultOptions = Options()


class ShortRepeatRLE:
    def __init__(self):
        pass

    def write(self, bs, rep, value, opt=None):
        opt = opt or _defaultOptions
        if opt.signed:
            value = zigzag(value)
        w = widthInBytes(value)
        assert (w >= 1 and w <= 8)
        assert (rep >= 3 and rep <= 10)
        h = (0x0 << 6) | ((w - 1) << 3) | (rep - 3)
        bs.append(h)
        bs.writeInt(value, w)

    def read(self, bs, opt=None):
        opt = opt or _defaultOptions
        b = bs.read()
        w = ((b >> 3) & 0x7) + 1
        rep = b & 0x7
        value = bs.readInt(w)
        if opt.signed:
            value = unzigzag(value)
        return [value] * (rep + 3)


def buildWbToEv():
    t = [-1] * 65
    t[0] = 0  # ???
    t[1] = 0
    t[2] = 1
    t[4] = 3
    t[8] = 7
    t[16] = 15
    t[24] = 23
    t[32] = 27
    t[40] = 28
    t[48] = 29
    t[56] = 30
    t[64] = 31
    t[3] = 2
    t[26] = 24
    t[28] = 25
    t[30] = 26

    for i in range(5, 7 + 1):
        t[i] = i - 1
    for i in range(9, 15 + 1):
        t[i] = i - 1
    for i in range(17, 21 + 1):
        t[i] = i - 1

    t2 = [-1] * 32
    for i in range(65):
        if t[i] == -1: continue
        t2[t[i]] = i
    return t, t2


_wb2ev, _ev2wb = buildWbToEv()


def widthBitsToEncodedValue(w):
    assert w <= 64
    assert _wb2ev[w] != -1
    return _wb2ev[w]


def encodeValueToWidthBits(ev):
    assert ev <= 31
    assert _ev2wb[ev] != -1
    return _ev2wb[ev]


_alignedBits = [0, 1, 2, 4, 4, 8, 8, 8, 8]


def alignedBits(b):
    if b < 8:
        return _alignedBits[b]
    return (b + 7) // 8 * 8


def encodeValuesWithFixedBits(wb, values, bs):
    if wb % 8 == 0:
        t = wb // 8
        for v in values:
            for i in reversed(range(t)):
                bs.append((v >> (i * 8)) & 0xff)
        return

    b = 0
    rem = 8
    for v in values:
        sz = wb
        while sz:
            take = min(rem, sz)
            mask = (1 << take) - 1
            b = (b << take) | ((v >> (sz - take)) & mask)
            sz -= take
            rem -= take
            if rem == 0:
                bs.append(b)
                b = 0
                rem = 8
    if rem != 8:
        b = b << rem
        bs.append(b)
    return


def decodeValuesWithFixedBits(wb, bs, bits):
    sz = (bits + 7) // 8
    buf = bs.read(sz)
    values = []

    if wb % 8 == 0:
        t = wb // 8
        assert sz % t == 0

        value = 0
        rep = t
        for i in range(sz):
            value = (value << 8) | buf[i]
            rep -= 1
            if rep == 0:
                values.append(value)
                rep = t
                value = 0
        return values

    value = 0
    need = wb
    for i in range(sz):
        b = buf[i]
        rem = 8

        while rem > 0:
            take = min(rem, need)
            mask = (1 << take) - 1
            shift = (rem - take)
            value = (value << take) | ((b >> shift) & mask)
            rem -= take
            need -= take
            if need == 0:
                values.append(value)
                need = wb
                value = 0
    return values


def zigzagValues(values):
    for i in range(len(values)):
        values[i] = zigzag(values[i])


def unzigzagValues(values):
    for i in range(len(values)):
        values[i] = unzigzag(values[i])


class DirectRLE:
    def __init__(self):
        pass

    def write(self, bs, values, opt=None):
        opt = opt or _defaultOptions
        wb = 0
        if opt.signed:
            zigzagValues(values)
        for v in values:
            x = widthInBits(v)
            wb = max(wb, x)
        if opt.aligned:
            wb = alignedBits(wb)

        ev = widthBitsToEncodedValue(wb)
        sz = len(values)
        h0 = (0x1 << 6) | (ev << 1) | (((sz - 1) >> 8) & 0x1)
        h1 = (sz - 1) & 0xff
        bs.extend([h0, h1])
        encodeValuesWithFixedBits(wb, values, bs)

    def read(self, bs, opt=None):
        opt = opt or _defaultOptions
        b0, b1 = bs.read(2)
        ev = (b0 >> 1) & 31
        wb = encodeValueToWidthBits(ev)
        l = ((b0 & 1) << 8) + b1 + 1
        bits = wb * l
        values = decodeValuesWithFixedBits(wb, bs, bits)
        if opt.signed:
            unzigzagValues(values)
        return values


class DeltaRLE:
    def __init__(self):
        pass

    def _write(self, bs, baseValue, baseDelta, deltas, opt):
        assert baseDelta != 0
        opt = opt or _defaultOptions
        wb = 0
        for d in deltas:
            # already abs called abs
            assert d >= 0
            x = widthInBits(d)
            wb = max(wb, x)

        if opt.aligned:
            wb = alignedBits(wb)
        ev = widthBitsToEncodedValue(wb)
        sz = len(deltas) + 2

        h0 = (0x3 << 6) | (ev << 1) | (((sz - 1) >> 8) & 0x1)
        h1 = (sz - 1) & 0xff
        bs.extend([h0, h1])

        if opt.signed:
            baseValue = zigzag(baseValue)
        _encode_varint(baseValue, bs)
        _encode_varint(zigzag(baseDelta), bs)
        encodeValuesWithFixedBits(wb, deltas, bs)

    def write(self, bs, values, opt=None):
        baseValue = values[0]
        baseDelta = values[1] - values[0]
        deltas = []
        for i in range(2, len(values)):
            d = values[i] - values[i - 1]
            assert d * baseDelta >= 0
            deltas.append(abs(d))
        return self._write(bs, baseValue, baseDelta, deltas, opt)

    def read(self, bs, opt=None):
        b0, b1 = bs.read(2)
        ev = (b0 >> 1) & 31
        wb = encodeValueToWidthBits(ev)
        l = ((b0 & 0x1) << 8) + b1 + 1

        baseValue = bs.decodeVarint()
        if opt.signed:
            baseValue = unzigzag(baseValue)

        baseDelta = bs.decodeVarint()
        baseDelta = unzigzag(baseDelta)
        # print(wb, l, baseValue, baseDelta)

        bits = wb * (l - 2)
        deltas = decodeValuesWithFixedBits(wb, bs, bits)
        values = [baseValue, baseValue + baseDelta]
        if baseDelta > 0:
            for d in deltas:
                values.append(values[-1] + d)
        else:
            for d in deltas:
                values.append(values[-1] - d)
        return values


def selectBaseAndGapWidth(values, pct=0.95):
    sz = len(values)
    temp = sorted(values)
    base = temp[0]
    for i in range(1, sz):
        temp[i] -= base

    pct = 0.95
    pivot = int(sz * pct)
    if pivot >= (sz - 1):
        pivot -= 1

    w = 0
    for i in range(1, pivot):
        v = widthInBits(temp[i])
        w = max(w, v)

    pw = w
    for i in range(pivot, len(values)):
        v = widthInBits(temp[i])
        pw = max(pw, v)

    assert (w < pw)
    return base, w, pw - w


class PatchBasedRLE:
    def __init__(self):
        pass

    def write(self, bs, values, opt=None):
        opt = opt or _defaultOptions
        base, w, pw = selectBaseAndGapWidth(values)
        # pack pgw and pw into at most 64 bits and aligned with bytes.
        if pw > 56:
            w = 8
            pw = 56

        if opt.aligned:
            w = alignedBits(w)
            # since pw + pgw will be packed together
            # no need to alignedBits here.
            # pw = alignedBits(pw)

        patch = []
        prev = 0
        thres = (1 << w) - 1
        pgw = 0
        sz = len(values)
        deltas = []
        for i in range(sz):
            x = values[i]
            delta = (x - base)
            assert delta >= 0
            deltas.append(delta)
            if delta > thres:
                gap = i - prev
                patch.append((gap, i))
                prev = i
                # pgw at most 8 bits
                # so max values is 255
                if gap > 255:
                    pgw = max(pgw, 8)
                else:
                    pgw = max(pgw, widthInBits(gap))

        ev = widthBitsToEncodedValue(w)
        pev = widthBitsToEncodedValue(pw)
        bw = widthInBytes(base)
        pll = len(patch)

        tmp = []
        mask = (1 << pw) - 1
        for (gap, index) in patch:
            v = (deltas[index] >> w)
            while gap > 255:
                tmp.append((0xff << pw) | 0)
                gap -= 255
            tmp.append((gap << pw) | (v & mask))
        # this is real pll.
        pll = len(tmp)

        # print(w, sz, bw, pw, pgw, pll, base, pw + pgw)
        h0 = (0x2 << 6) | (ev << 1) | (((sz - 1) >> 8) & 0x1)
        h1 = (sz - 1) & 0xff
        h2 = ((bw - 1) << 5) | (pw - 1)
        h3 = ((pgw - 1) << 5) | pll

        bs.extend([h0, h1, h2, h3])
        bs.writeInt(base, bw)
        encodeValuesWithFixedBits(w, deltas, bs)

        wb = (pgw + pw)
        if opt.aligned:
            wb = alignedBits(wb)
        encodeValuesWithFixedBits(wb, tmp, bs)

    def read(self, bs, opt=None):
        opt = opt or _defaultOptions
        h0, h1, h2, h3 = bs.read(4)
        ev = (h0 >> 1) & 31
        w = encodeValueToWidthBits(ev)
        l = ((h0 & 0x1) << 8) + h1 + 1
        bw = ((h2 >> 5) & 7) + 1
        pw = encodeValueToWidthBits(h2 & 31)
        pgw = ((h3 >> 5) & 7) + 1
        pll = h3 & 31

        # print(w, l, bw, pw, pgw, pll)
        base = bs.readInt(bw)
        bits = w * l
        deltas = decodeValuesWithFixedBits(w, bs, bits)

        wb = (pw + pgw)
        if opt.aligned:
            wb = alignedBits(wb)
        bits = wb * pll
        tmp = decodeValuesWithFixedBits(wb, bs, bits)
        prev = 0
        gap = 0

        pgwshift = (wb - pgw)
        pgwmask = (1 << pgw) - 1
        pwshift = (wb - pgw - pw)
        pwmask = (1 << pw) - 1

        for x in tmp:
            g = (x >> pgwshift) & pgwmask
            p = (x >> pwshift) & pwmask
            gap = (gap << 8) + g
            if p == 0:
                assert g == 255
                continue
            else:
                index = gap + prev
                deltas[index] |= (p << w)
                prev = index

        values = deltas
        for i in range(l):
            values[i] += base
        return values


# ==================== UT  ====================

class TestAll(unittest.TestCase):
    def test_zigzag(self):
        raw = list(range(-10, 10))
        for x in raw:
            y = zigzag(x)
            exp = x * 2
            if x < 0:
                exp = -exp - 1
            self.assertEqual(y, exp)

        raw = list(range(-10, 10))
        output = [zigzag(x) for x in raw]
        back = [unzigzag(x) for x in output]
        self.assertTrue(raw == back)

    def test_encode_varint(self):
        self.assertEqual(encode_varint(0), b'\x00')
        self.assertEqual(encode_varint(1), b'\x01')
        self.assertEqual(encode_varint(127), b'\x7f')
        self.assertEqual(encode_varint(128), b'\x80\x01')
        self.assertEqual(encode_varint(129), b'\x81\x01')
        self.assertEqual(encode_varint(16383), b'\xff\x7f')
        self.assertEqual(encode_varint(16384), b'\x80\x80\x01')
        self.assertEqual(encode_varint(16385), b'\x81\x80\x01')

    def test_varint(self):
        for x in range(10, 32000, 100):
            bs = encode_varint(x)
            y = decode_varint(bs)
            self.assertEqual(
                x, y, "bs = {}".format(bs))

    def test_byterle(self):
        leastRepeat = 3
        rle = ByteRLE(leastRepeat)
        decoder = ByteRLEDecoder()
        for sz in range(4, 20):
            rle.reset()
            buf = [0] * sz
            rle.addMany(buf)
            rle.flush()
            bs = rle.getBytes()
            exp = bytes([sz - leastRepeat]) + b'\x00'
            self.assertEqual(bs, exp)
            buf2 = decoder.decode(bs)
            self.assertEqual(buf, buf2)

        rle.reset()
        size = 20
        buf = [i + 0x40 for i in range(size)]
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = bytes([-size & 0xff] + [x + 0x40 for x in range(size)])
        self.assertEqual(bs, exp)
        buf2 = decoder.decode(bs)
        self.assertEqual(buf, buf2)

        rle.reset()
        size = 20
        a = [i + 0x40 for i in range(size)]
        b = [0] * size
        buf = a + b + a + b
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        x = bytes([-size & 0xff] + [x + 0x40 for x in range(size)])
        y = bytes([size - leastRepeat]) + b'\x00'
        exp = x + y + x + y
        self.assertEqual(bs, exp)
        buf2 = decoder.decode(bs)
        self.assertEqual(buf, buf2)

    def test_bitrle(self):
        leastRepeat = 3
        rle = BitRLE(leastRepeat)
        bits = [1] + [0] * 7
        rle.addMany(bits)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\xff\x80'
        self.assertEqual(bs, exp)
        decoder = BitRLEDecoder()
        bits2 = decoder.decode(bs, 8)
        self.assertEqual(bits, bits2)

    def test_rlev1(self):
        leastRepeat = 3
        rle = RLEv1(leastRepeat)

        rle.reset()
        buf = [7] * 100
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\x61\x00\x07'
        self.assertEqual(bs, exp)

        rle.reset()
        buf = list(reversed(range(1, 100 + 1)))
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\x61\xff\x64'
        self.assertEqual(bs, exp)

        rle.reset()
        buf = [2, 3, 6, 7, 11]
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\xfb\x02\x03\x06\x07\x0b'
        self.assertEqual(bs, exp)

        rle.reset()
        buf = [2, 3, 4, 7, 11]
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\x00\x01\x02\xfe\x07\x0b'
        self.assertEqual(bs, exp)

        rle.reset()
        buf = [2, 3, 5, 7, 11]
        rle.addMany(buf)
        rle.flush()
        bs = rle.getBytes()
        exp = b'\xff\x02\x00\x02\x03\xff\x0b'
        self.assertEqual(bs, exp)

    def test_stringencoder(self):
        encoder = StringEncoder()
        decoder = StringDecoder()
        buf = ["Nevada", "California"]
        encoder.addMany(buf)
        data, length = encoder.encodeDirect()
        self.assertEqual(data, "NevadaCalifornia")
        self.assertEqual(length, [6, 10])
        buf2 = decoder.decodeDirect(data, length)
        self.assertEqual(buf, buf2)

        encoder.reset()
        buf = ["Nevada", "California", "Nevada", "California", "Florida"]
        encoder.addMany(buf)
        ddata, length, data = encoder.encodeDictionary()
        self.assertEqual(ddata, "CaliforniaFloridaNevada")
        self.assertEqual(length, [10, 7, 6])
        self.assertEqual(data, [2, 0, 2, 0, 1])
        buf2 = decoder.decodeDictinary(ddata, length, data)
        self.assertEqual(buf, buf2)

    def test_utility(self):
        self.assertEqual(widthInBits(0), 1)
        self.assertEqual(widthInBits(1), 1)
        self.assertEqual(widthInBits(2), 2)
        self.assertEqual(widthInBits(3), 2)

    def test_shortrepeatrle(self):
        rle = ShortRepeatRLE()
        bs = OutputByteStream()
        rle.write(bs, 5, 10000)
        self.assertEqual(bs.asBytes(), b'\x0a\x27\x10')
        bs = InputByteStream(b'\x0a\x27\x10')
        self.assertEqual(rle.read(bs), [10000] * 5)

    def test_directrle(self):
        opt = Options()
        opt.aligned = False
        rle = DirectRLE()
        values = [23713, 43806, 57005, 48879]
        exp = b'\x5e\x03\x5c\xa1\xab\x1e\xde\xad\xbe\xef'
        bs = OutputByteStream()
        rle.write(bs, values, opt)
        self.assertEqual(bs.asBytes(), exp)
        bs = InputByteStream(exp)
        self.assertEqual(rle.read(bs, opt), values)

    def test_deltarle(self):
        opt = Options()
        opt.aligned = True
        rle = DeltaRLE()
        values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        exp = b'\xc6\x09\x02\x02\x22\x42\x42\x46'
        bs = OutputByteStream()
        rle.write(bs, values, opt)
        self.assertEqual(bs.asBytes(), exp)
        bs = InputByteStream(exp)
        self.assertEqual(rle.read(bs, opt), values)

    def test_patchbasedrle(self):
        opt = Options()
        opt.aligned = False
        rle = PatchBasedRLE()
        values = [2030, 2000, 2020, 1000000, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150,
                  2160, 2170, 2180, 2190]
        exp = bytes(
            [0x8e, 0x13, 0x2b, 0x21, 0x07, 0xd0, 0x1e, 0x00, 0x14, 0x70, 0x28, 0x32, 0x3c, 0x46, 0x50, 0x5a, 0x64, 0x6e,
             0x78, 0x82, 0x8c, 0x96, 0xa0, 0xaa, 0xb4, 0xbe, 0xfc, 0xe8])
        bs = OutputByteStream()
        rle.write(bs, values, opt)
        self.assertEqual(bs.asBytes(), exp)
        bs = InputByteStream(exp)
        self.assertEqual(rle.read(bs, opt), values)


if __name__ == '__main__':
    unittest.main()
