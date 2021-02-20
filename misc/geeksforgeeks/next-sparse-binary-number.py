#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n):
    p = 0
    while p <= 30:
        if (n >> p) & 0x1 and (n >> (p + 1)) & 0x1:
            n += (1 << p)
            n &= ~((1 << p) - 1)
        p += 1
    return n


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
