#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n):
    base = 1
    res = 0
    for i in range(0, 32):
        if (n >> i) & 0x1:
            res += base
        base *= 7
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
