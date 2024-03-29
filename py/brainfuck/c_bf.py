#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import array
import sys

import simple_bf
from bytecode import Bytecode, Compare, CompilerFlags, Instr as I, Label
from bytecode.peephole_opt import PeepholeOptimizer

def gen_c_code(fh, ops):
    cs = []
    labels = []
    L = 0

    for c, rep in ops:
        if c == '>' or c == '<':
            # ptr += rep
            if c == '<':
                rep = -rep
            cs.append('ptr += %d;' % rep)

        elif c == '+' or c == '-':
            # *ptr += rep
            if c == '-':
                rep = -rep
            # cs.append('*ptr = (*ptr + %d) & 0xff;' % rep)
            cs.append('*ptr = (*ptr + %d);' % rep)

        elif c == '0':
            cs.append('*ptr = 0;')

        elif c == '.':
            cs.append("sys_write(*ptr, %d);" % rep)
        elif c == ',':
            cs.append("*ptr = sys_read(%d);" % rep)

        elif c == '[':
            start, end  = 'L%d' % L, 'L%d' % (L+1)
            L += 2
            labels.append((start, end))
            code = "if(*ptr == 0) goto {end};\n{start}:;".format(start = start, end = end)
            cs.append(code)

        elif c == ']':
            start, end = labels.pop()
            code = "if (*ptr !=0) goto {start};\n{end}:;".format(start = start, end = end)
            cs.append(code)

        else:
            pass

    fh.write("void sys_write(unsigned char c, int rep);\n")
    fh.write("unsigned char sys_read(int rep);\n")
    fh.write("char mem[1024000];\nchar* ptr=mem;\n")
    fh.write("void __f() {\n")
    fh.write("\n".join(cs))
    fh.write("}\nint main() { __f(); return 0;}\n");

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--cc', action='store', default='gcc')
    parser.add_argument('--optlevel', action='store', default=0, type=int)
    parser.add_argument('--filepath', action='store')

    args = parser.parse_args()
    file_path = args.filepath
    optlevel = args.optlevel
    cc = args.cc
    if not file_path:
        return
    if not file_path.endswith('.bf'):
        print('file: %s not a brainfuck program' % file_path)
        return

    with open(file_path) as fh:
        data = fh.read()

    import time
    a = time.time()
    ops = simple_bf.optimize_source(data)
    with open('c_bf.c', 'w') as fh:
        gen_c_code(fh, ops)
    b = time.time()

    import subprocess
    ret = subprocess.run(('%s -O%d -o /tmp/c_bf.exe c_bf.c libio.so' % (cc, optlevel)).split())
    if ret.returncode != 0:
        return
    c = time.time()

    subprocess.run('/tmp/c_bf.exe'.split())
    d = time.time()

    print('cc = %s, optlevel = %d, code time = %.2fms, compile time = %.2fms, run time = %.2fms' % (cc, optlevel, b-a, c-b, d-c))


if __name__ == '__main__':
    main()
