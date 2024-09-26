#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import itertools


def solve(data):
    dist = {}
    nodes = set()
    for s in data:
        ss = s.split()
        x, y, d = ss[0], ss[2], ss[4]
        d = int(d)
        nodes.add(x)
        nodes.add(y)
        dist[(x, y)] = d

    nodes = list(nodes)
    ans = 1 << 63
    for seq in itertools.permutations(nodes):
        r = 0
        p = None
        for x in seq:
            if p is None:
                p = x
                continue
            d = dist.get((x, p)) or dist.get((p, x))
            r += d
            p = x
        ans = min(ans, r)
    return ans


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    with open(input_file) as fh:
        data = [s.strip() for s in fh]
        ans = solve(data)

    print(ans)


if __name__ == '__main__':
    main()
