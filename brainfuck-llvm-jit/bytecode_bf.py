#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import array
import sys

import simple_bf
from bytecode import Bytecode, Compare, CompilerFlags, Instr as I, Label
from bytecode.peephole_opt import PeepholeOptimizer


def run_bytecode(ops):
    cs = []
    labels = []
    patches = []

    for c, rep in ops:
        if c == '>' or c == '<':
            # ptr += rep
            if c == '<':
                rep = -rep

            codes = [
                I("LOAD_FAST", "ptr"),
                I("LOAD_CONST", rep),
                I("BINARY_ADD"),
                I("STORE_FAST", "ptr"),
            ]
            cs.extend(codes)

        elif c == '+' or c == '-':
            # *ptr += rep
            if c == '-':
                rep = -rep

            codes = [
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("DUP_TOP_TWO"),
                I("BINARY_SUBSCR"),
                I("LOAD_CONST", rep),
                I("BINARY_ADD"),
                I("LOAD_CONST", 0xff),
                I("BINARY_AND"),
                I("ROT_THREE"),
                I("STORE_SUBSCR"),
            ]
            cs.extend(codes)

        elif c == '0':
            # *ptr = 0
            codes = [
                I("LOAD_CONST", 0),
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("STORE_SUBSCR")
            ]
            cs.extend(codes)

        elif c == '.':
            codes = [
                I("LOAD_FAST", "sys_write"),
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("BINARY_SUBSCR"),
                I("LOAD_CONST", rep),
                I("CALL_FUNCTION", 2),
                I("POP_TOP")
            ]
            cs.extend(codes)

        elif c == ',':
            codes = [
                I("LOAD_FAST", "sys_read"),
                I("LOAD_CONST", rep),
                I("CALL_FUNCTION", 1),
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("STORE_SUBSCR")
            ]
            cs.extend(codes)

        elif c == '[':
            start_label = Label()
            codes = [
                start_label,
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("BINARY_SUBSCR"),
                I("LOAD_CONST", 0),
                I("COMPARE_OP", Compare.EQ),
                None,
            ]
            cs.extend(codes)
            labels.append(start_label)
            patches.append(len(cs) - 1)

        elif c == ']':
            start_label = labels.pop()
            end_label = Label()
            pp = patches.pop()
            cs[pp] = I("POP_JUMP_IF_TRUE", end_label)
            codes = [
                end_label,
                I("LOAD_FAST", "mem"),
                I("LOAD_FAST", "ptr"),
                I("BINARY_SUBSCR"),
                I("LOAD_CONST", 0),
                I("COMPARE_OP", Compare.EQ),
                I("POP_JUMP_IF_FALSE", start_label)
            ]
            cs.extend(codes)

    cs.extend([I("LOAD_CONST", None), I("RETURN_VALUE")])
    assert not labels and not patches
    for x in cs:
        print(x)

    def sys_write(c, rep):
        sys.stdout.write(chr(c) * rep)
        sys.stdout.flush()

    def sys_read(rep):
        data = sys.stdin.read(rep)
        return ord(data[-1]) & 0xff

    mem_size = 10 ** 6
    env = dict(
        mem=array.array('B', [0] * mem_size),
        ptr=0,
        sys_read=sys_read,
        sys_write=sys_write
    )

    load_cs = []
    for k in env:
        load_cs.extend([
            I("LOAD_NAME", k),
            I("STORE_FAST", k)
        ])
    bc = Bytecode(load_cs + cs)
    bc.flags = CompilerFlags(CompilerFlags.OPTIMIZED)
    code = PeepholeOptimizer().optimize(bc.to_code())
    exec(code, {}, env)


def main():
    file_path = sys.argv[-1]
    with open(file_path) as fh:
        data = fh.read()

    ops = simple_bf.optimize_source(data)
    run_bytecode(ops)


if __name__ == '__main__':
    main()
