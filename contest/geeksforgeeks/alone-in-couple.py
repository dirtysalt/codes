#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(xs):
    res = 0
    for x in xs:
        res ^= x
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
