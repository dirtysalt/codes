#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import array
import sys

from bytecode import Bytecode, Compare, Instr as I, Label


class Memory:
    def __init__(self, size=1000000):
        self.data = array.array('B', [0] * size)
        self.addr = 0
        self.size = size

    def ensure_size(self, addr):
        n = self.size
        if addr < n:
            return

        while addr >= n:
            n = n * 2
        self.data.extend([0] * (n - self.size))
        self.size = n

    def get(self):
        self.ensure_size(self.addr)
        return self.data[self.addr]

    def set(self, v):
        self.ensure_size(self.addr)
        self.data[self.addr] = v

    def increase(self, rep=1):
        self.ensure_size(self.addr)
        v = self.data[self.addr]
        self.data[self.addr] = (v + rep) & 0x0ff

    def decrease(self, rep=1):
        self.ensure_size(self.addr)
        v = self.data[self.addr]
        self.data[self.addr] = (v - rep) & 0x0ff

    def forward(self, rep=1):
        self.addr += rep

    def backward(self, rep=1):
        self.addr -= rep

    def write(self, rep=1):
        v = self.get()
        for i in range(rep):
            sys.stdout.write(chr(v))
        sys.stdout.flush()

    def read(self, rep=1):
        for i in range(rep):
            c = sys.stdin.read(1)
        self.set(ord(c))

    def zero(self, rep=1):
        self.data[self.addr] = 0


def optimize_source(s):
    s = [c for c in s if c in '><+-.,[]']

    # fold to (op, count)
    ops = []
    prev = None
    count = 0
    for c in s:
        if c in '[]' or c != prev:
            if prev:
                ops.append((prev, count))
            prev = c
            count = 1
        else:
            count += 1
    if prev:
        ops.append((prev, count))

    # optimize [-] to zero current cell
    i = 0
    while i < len(ops) - 2:
        a, ac = ops[i]
        b, bc = ops[i + 1]
        c, cc = ops[i + 2]
        if a == '[' and b == '-' and bc == 1 and c == ']':
            ops[i] = ('0', 1)
            ops[i + 1] = None
            ops[i + 2] = None
            i += 2
        i += 1

    # remove all None
    ops = [x for x in ops if x is not None]
    return ops


def run_optimized(ops):
    jumps = {}
    st = []
    for i, (op, c) in enumerate(ops):
        if op == '[':
            st.append(i)
        elif op == ']':
            x = st.pop()
            jumps[x] = i
            jumps[i] = x

    # print(ops)
    mem = Memory()
    pc = 0
    sz = len(ops)
    while pc < sz:
        c, rep = ops[pc]
        if c == '>':
            mem.forward(rep)
        elif c == '<':
            mem.backward(rep)
        elif c == '+':
            mem.increase(rep)
        elif c == '-':
            mem.decrease(rep)
        elif c == '.':
            mem.write(rep)
        elif c == ',':
            mem.read(rep)
        elif c == '[':
            if mem.get() == 0:
                pc = jumps[pc]
        elif c == ']':
            if mem.get() != 0:
                pc = jumps[pc]
        elif c == '0':
            mem.zero()
        else:
            pass
        pc += 1


def run_bytecode(ops):
    def call_mem(name, rep):
        codes = [
            I("LOAD_FAST", "mem"),
            I("LOAD_ATTR", name),
            I("LOAD_CONST", rep),
            I("CALL_FUNCTION", 1),
            I("POP_TOP")
        ]
        return codes

    mapping = {
        '>': 'forward',
        '<': 'backward',
        '+': 'increase',
        '-': 'decrease',
        '.': 'write',
        ',': 'read',
        '0': 'zero'
    }

    cs = []
    labels = []
    patches = []

    for c, rep in ops:
        if c in mapping:
            codes = call_mem(mapping[c], rep)
            cs.extend(codes)
        elif c == '[':
            start_label = Label()
            codes = [
                start_label,
                I("LOAD_FAST", "mem"),
                I("LOAD_ATTR", "get"),
                I("CALL_FUNCTION", 0),
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
                I("LOAD_ATTR", "get"),
                I("CALL_FUNCTION", 0),
                I("LOAD_CONST", 0),
                I("COMPARE_OP", Compare.EQ),
                I("POP_JUMP_IF_FALSE", start_label)
            ]
            cs.extend(codes)

    cs.extend([I("LOAD_CONST", None), I("RETURN_VALUE")])
    assert not labels and not patches

    # for x in cs:
    #     print(x)

    def run(cs):
        mem = Memory()
        load_cs = [
            I("LOAD_NAME", "mem"),
            I("STORE_FAST", "mem")
        ]
        code = Bytecode(load_cs + cs).to_code()
        exec(code, {}, {'mem': mem})

    run(cs)


def run_naive(s):
    jumps = {}
    st = []
    for i, c in enumerate(s):
        if c == '[':
            st.append(i)
        elif c == ']':
            x = st.pop()
            jumps[x] = i
            jumps[i] = x

    mem = Memory()
    pc = 0
    sz = len(s)
    while pc < sz:
        c = s[pc]
        if c == '>':
            mem.forward()
        elif c == '<':
            mem.backward()
        elif c == '+':
            mem.increase()
        elif c == '-':
            mem.decrease()
        elif c == '.':
            mem.write()
        elif c == ',':
            mem.read()
        elif c == '[':
            if mem.get() == 0:
                pc = jumps[pc]
        elif c == ']':
            if mem.get() != 0:
                pc = jumps[pc]
        else:
            pass
        pc += 1


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--optimize', action='store_true')
    parser.add_argument('--bytecode', action='store_true')
    parser.add_argument('--filepath', action='store')

    args = parser.parse_args()
    file_path = args.filepath
    if not file_path:
        return

    with open(file_path) as fh:
        data = fh.read()

    if args.optimize:
        ops = optimize_source(data)
        run_optimized(ops)
    elif args.bytecode:
        ops = optimize_source(data)
        run_bytecode(ops)
    else:
        run_naive(data)


if __name__ == '__main__':
    main()
