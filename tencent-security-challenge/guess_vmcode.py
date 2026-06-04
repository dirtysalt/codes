#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import base64

ins_len = [1] * 5 + [2] * 9 + [9, 1]
reg = [0] * 16
code = base64.b64decode('zyLpMs8CL9Oy/3QDdRlURZRGFHQHdRhURZFGIL/lv+MiNi+70AXRBtMD1wfYCNkJ5v3/iV14RWMB0n+/xgk=')

texts = [
    "quit",
    "push R{r0}",
    "pop R{r0}",
    "if not R{r0}: R15 += {sz}",
    "R{r0} = 1 - R{r0}",
    "R{r0} = R{r1} + R{r2}",
    "R{r0} = R{r1} - R{r2}",
    "R{r0} = R{r1} * R{r2}",
    "R{r0} = R{r1} / R{r2}",
    "R{r0} = R{r1} % R{r2}",
    "R{r0} = 1 if R{r1} < R{r2} else 0",
    "push R{r0}; R{r0} += {arg}",
    "R{r0} += {arg}",
    "R{r0} = {arg}",
    "R{r0} = {arg}"
]

assert len(texts) == 15

offsets = [0, 3, 4, 6, 8, 10, 12, 14, 16, 18, 19, 21, 23, 25, 27, 28, 30, 32, 33, 34,
           36, 38, 40, 42, 44, 46, 48, 57, 59, 61]


def disassemble(code):
    for off in offsets:
        i = off
        ins, r0 = code[i] >> 4, code[i] & 15
        length = ins_len[ins]
        arg, r1, r2 = [None] * 3
        if length > 1:
            arg = code[i + 1: i + length]
            if length == 2: r1 = arg[0] >> 4; r2 = arg[0] & 15

        temp = texts[ins]
        if arg is not None:
            arg = int.from_bytes(arg, byteorder='little', signed=True)
        t = temp.format(arg=arg, r0=r0, r1=r1, r2=r2, sz=length)
        print('%03d:\tR15 += %d\t' % (off, length) + t)


disassemble(code)

stack = []
pc = set()
loops = 0

insts = 100000
while insts:
    insts -= 1
    pc.add(reg[15])
    off = reg[15]
    ins, r0 = code[reg[15]] >> 4, code[reg[15]] & 15
    length = ins_len[ins]
    arg, r1, r2 = [None] * 3
    if length > 1:
        arg = code[reg[15] + 1: reg[15] + length]
        if length == 2: r1 = arg[0] >> 4; r2 = arg[0] & 15
    reg[15] += length
    if 0 == ins:
        break
    elif 1 == ins:
        stack.append(reg[r0])
    elif 2 == ins:
        if off == 27:
            loops += 1
        reg[r0] = stack.pop()
    elif 3 == ins:
        if not reg[r0]: reg[15] += ins_len[code[reg[15]] >> 4]
    elif 4 == ins:
        reg[r0] = 0 if reg[r0] else 1
    elif 5 == ins:
        reg[r0] = reg[r1] + reg[r2]
    elif 6 == ins:
        reg[r0] = reg[r1] - reg[r2]
    elif 7 == ins:
        reg[r0] = reg[r1] * reg[r2]
    elif 8 == ins:
        reg[r0] = reg[r1] / reg[r2]
    elif 9 == ins:
        reg[r0] = reg[r1] % reg[r2]
    elif 10 == ins:
        reg[r0] = 1 if reg[r1] < reg[r2] else 0
    elif 11 == ins:
        stack.append(reg[r0]);
        reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
    elif 12 == ins:
        reg[r0] += int.from_bytes(arg, byteorder='little', signed=True)
    elif ins in (13, 14):
        if off == 57:
            print('>>>', int.from_bytes(arg, byteorder='little', signed=True))
            # change 127 to 3
            # 3 -> 7
            # 4 -> 15
            # 5 -> 31
            # 127 -> 2^127-1
            reg[r0] = 3
        else:
            reg[r0] = int.from_bytes(arg, byteorder='little', signed=True)

    # temp = texts[ins]
    # if arg is not None:
    #     arg = int.from_bytes(arg, byteorder='little', signed=True)
    # t = temp.format(arg=arg, r0=r0, r1=r1, r2=r2, sz=length)
    # print(t)

print(sorted(pc))
print(offsets)
assert sorted(pc) == offsets
#
print('>>>', loops)
print(reg[0], reg[1])

MOD = 99999999999999997
rs = [0] * 16
rs[0] = 5
rs[1] = 6
rs[3] = 3
rs[7] = 7
rs[8] = 8
rs[9] = 9
rs[6] = MOD
for i in range(loops):
    r = rs
    a = (r[0] * r[3] + r[1] * r[9]) % r[6]
    b = (r[0] * r[7] + r[1] * r[8]) % r[6]
    r[0], r[1] = a, b
print(rs[0], rs[1])
