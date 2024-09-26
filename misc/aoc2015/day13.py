#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import itertools


def solve(costs):
    pp = set()
    for (a, b), d in costs.items():
        pp.add(a)
        pp.add(b)

    pp = list(pp)

    ans = -(1 << 63)
    for seq in itertools.permutations(pp):
        value = 0
        for i in range(len(seq)):
            a, b = seq[i], seq[((i - 1) + len(seq)) % len(seq)]
            a, c = seq[i], seq[(i + 1) % len(seq)]
            value += costs[(a, b)]
            value += costs[(a, c)]
        ans = max(value, ans)

    return ans


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    costs = {}
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            ss = s.split()
            a, b, c, d = ss[0], ss[-1][:-1], ss[2], ss[3]
            d = int(d)
            if c == 'lose':
                d = -d
            costs[(a, b)] = d

    ans = solve(costs)
    print(ans)


if __name__ == '__main__':
    main()
