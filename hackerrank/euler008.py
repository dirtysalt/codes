#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, k, num):
    max_res = 0
    for i in range(0, n - k + 1):
        res = 1
        for j in range(i, i + k):
            res *= int(num[j])
        max_res = max(max_res, res)
    return max_res


t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    num = input().strip()
    print((solve(n, k, num)))
