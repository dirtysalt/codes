#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n):
    a = 1
    b = 1
    res = 0
    while a < n:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
