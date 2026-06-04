#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(reg, opcodes):
    pc = 0

    def getvalue(operand):
        if operand in (0, 1, 2, 3):
            return operand
        if operand in (4, 5, 6):
            return reg[operand - 4]

    out = []
    while pc < len(opcodes):
        op, operand = opcodes[pc: pc + 2]
        value = getvalue(operand)
        pc += 2
        if op == 0:
            reg[0] = reg[0] // (2 ** value)
        elif op == 1:
            reg[1] = reg[1] ^ operand
        elif op == 2:
            reg[1] = value % 8
        elif op == 3:
            if reg[0] != 0:
                pc = operand
        elif op == 4:
            reg[1] = reg[1] ^ reg[2]
        elif op == 5:
            out.append(value % 8)
        elif op == 6:
            reg[1] = reg[0] // (2 ** value)
        elif op == 7:
            reg[2] = reg[0] // (2 ** value)

    return reg, out


def test():
    reg, out = solve([0, 0, 9], [2, 6])
    assert reg[1] == 1

    reg, out = solve([10, 0, 0], [5, 0, 5, 1, 5, 4])
    assert out == [0, 1, 2]


test()


def main():
    input = 'tmp.in'
    reg = [0] * 3
    opcodes = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            a, b = s.split(': ')
            if a[-1] == 'A':
                reg[0] = int(b)
            elif a[-1] == 'B':
                reg[1] = int(b)
            elif a[-2] == 'C':
                reg[2] = int(b)
            else:
                opcodes = [int(x) for x in b.split(',')]
    print(reg, opcodes)
    reg, out = solve(reg, opcodes)
    print(','.join([str(x) for x in out]))


if __name__ == '__main__':
    main()
