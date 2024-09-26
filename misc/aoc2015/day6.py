#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(insts):
    def parse_inst(inst):
        ss = inst.split()
        if ss[0] == 'turn':
            value = 1 if ss[1] == 'on' else 0
            ss = ss[2:]
        else:
            value = -1
            ss = ss[1:]

        a, b = ss[0], ss[2]
        return value, [int(x) for x in a.split(',')], [int(x) for x in b.split(',')]

    N = 1000
    g = [[0] * N for _ in range(N)]
    for inst in insts:
        value, (x0, y0), (x1, y1) = parse_inst(inst)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if value == -1:
                    g[x][y] = 1 - g[x][y]
                else:
                    g[x][y] = value

    return sum([sum(x) for x in g])


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    insts = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            insts.append(s)

    ans = solve(insts)
    print(ans)


if __name__ == '__main__':
    main()
