#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def gcd(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a, b = b, c


def lcm(a, b):
    c = gcd(a, b)
    return a * b // c


def solve(n):
    res = 1
    for i in range(1, n + 1):
        res = lcm(res, i)
    return res


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
