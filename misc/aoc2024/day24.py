#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(values, wires):
    while wires:
        unsolved = []
        for op, x, y, z in wires:
            if x in values and y in values:
                x, y = values[x], values[y]
                v = 0
                if op == 'AND':
                    v = x & y
                elif op == 'OR':
                    v = x | y
                elif op == 'XOR':
                    v = x ^ y
                values[z] = v
            else:
                unsolved.append((op, x, y, z))
        wires = unsolved
    return values


def main():
    # input = 'debug.in'
    input = 'tmp.in'
    values = {}
    wires = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: break
            k, v = s.split(': ')
            values[k] = int(v)

        for s in fh:
            s = s.strip()
            a, b = s.split(' -> ')
            x, op, y = a.split()
            wires.append((op, x, y, b))

    values = solve(values, wires)
    keys = [k for k in values if k[0] == 'z']
    keys.sort(reverse=True)
    ans = []
    for k in keys:
        ans.append(values[k])
    print(ans)

    b = 0
    for x in ans:
        b = (b << 1) + x
    print(b)


if __name__ == '__main__':
    main()
