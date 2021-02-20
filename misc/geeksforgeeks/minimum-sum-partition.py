#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(xs):
    values = set([0])
    for x in xs:
        vals = set()
        for v in values:
            vals.add(x + v)
            vals.add(x - v)
        values = vals
    # print(values)
    values = [abs(x) for x in values]
    return min(values)


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
