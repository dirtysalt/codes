#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n):
    res = 0
    n3 = n // 3
    res += 3 * (1 + n3) * n3 // 2
    n5 = n // 5
    res += 5 * (1 + n5) * n5 // 2
    n15 = n // 15
    res -= 15 * (1 + n15) * n15 // 2
    return res


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
