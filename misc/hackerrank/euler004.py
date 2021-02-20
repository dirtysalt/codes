#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import bisect

knowns = set()
for a in range(100, 1000):
    for b in range(100, 1000):
        c = a * b
        cs = str(c)
        if cs == cs[::-1]:
            knowns.add(c)
knowns = list(knowns)
knowns.sort()


def solve(n):
    p = bisect.bisect_left(knowns, n)
    return knowns[p - 1]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
