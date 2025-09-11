#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(xs):
    sum_value = sum(xs)
    if sum_value % 2 != 0:
        return 'NO'
    exp_value = sum_value // 2

    values = set([0])
    for x in xs:
        vals = values.copy()
        for v in values:
            if (x + v) <= exp_value:
                vals.add(x + v)
        values = vals
        if exp_value in values:
            return 'YES'
    return 'NO'


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
