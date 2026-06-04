#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(orders):
    from collections import defaultdict
    adj = defaultdict(set)
    for x, y in orders:
        adj[x].add(y)
        adj[y].add(x)

    groups = set()
    for x in adj:
        if x[0] != 't': continue
        for y in adj[x]:
            for z in adj[x]:
                if z in adj[y]:
                    t = sorted([x, y, z])
                    groups.add(tuple(t))

    # print(groups)
    return len(groups)


def main():
    # input = 'debug.in'
    input = 'tmp.in'
    orders = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            orders.append(s.split('-'))

    print(solve(orders))


if __name__ == '__main__':
    main()
