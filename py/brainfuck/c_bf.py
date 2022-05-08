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
            cs.append('mem[ptr] = (mem[ptr] + %d) & 0xff;' % rep)

        elif c == '0':
            cs.append('mem[ptr] = 0;')

        elif c == '.':
            cs.append("{{ char _buf[{rep}+1]; _buf[{rep}]=0; memset(_buf, mem[ptr], {rep}); fprintf(stderr, \"%s\", _buf); }}".format(rep = rep))

        elif c == ',':
            cs.append("{{ char_buf[{rep}]; fread(_buf, 1, {rep}, stdin); mem[ptr] = _buf[{rep}-1]; }}".format(rep = rep))

        elif c == '[':
            start, end  = 'L%d' % L, 'L%d' % (L+1)
            L += 2
            labels.append((start, end))
            code = "if(mem[ptr] == 0) goto {end};\n{start}:;".format(start = start, end = end)
            cs.append(code)

        elif c == ']':
            start, end = labels.pop()
            code = "if (mem[ptr] !=0) goto {start};\n{end}:;".format(start = start, end = end)
            cs.append(code)

        else:
            print('unknown char %s' % c)
            pass

    fh.write("#include <stdio.h>\n")
    fh.write("#include <memory.h>\n")
    fh.write("char mem[1024000];\nint ptr=0;\n")
    fh.write("void __f() {\n")
    fh.write("\n".join(cs))
    fh.write("}\nint main() { __f(); return 0;}\n");

def main():
    file_path = sys.argv[-1]
    with open(file_path) as fh:
        data = fh.read()

    ops = simple_bf.optimize_source(data)
    with open('c_bf.c', 'w') as fh:
        gen_c_code(fh, ops)

if __name__ == '__main__':
    main()
