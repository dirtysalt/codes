#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 10 ** 4
result = [0] * (1 + N)
for i in range(2, N + 1):
    result[i] = result[i - 1] + \
                (i - 1) * i * i


def solve(n):
    return result[n]


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
