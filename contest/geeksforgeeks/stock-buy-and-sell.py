#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(xs):
    res = []
    n = len(xs)
    buy, sell = None, None
    for i in range(1, n):
        if xs[i] > xs[i - 1]:
            if buy is None:
                buy = (i - 1)
            if sell is None:
                sell = i

            if (i - sell) > 1:  # not contiguous
                res.append((buy, sell))
                buy = None
                sell = None
            else:
                sell = i
        else:
            if buy is not None and sell is not None:
                res.append((buy, sell))
                buy, sell = None, None

    if buy is not None and sell is not None:
        res.append((buy, sell))
    if res:
        return ' '.join(['({} {})'.format(x[0], x[1]) for x in res])
    return 'No Profit'


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
