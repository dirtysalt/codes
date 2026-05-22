#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 3000
table = [-1] * (N + 1)
for n in range(3, N + 1):
    res = -1
    for c in range(1, n // 2 + 1):
        ab2 = n * (n - 2 * c)
        if ab2 % 2 != 0:
            continue
        ab = ab2 // 2
        if ab * c < res:
            continue
        # a + b = c, a * b = ab
        # find a possible solution.
        x = c * c - 4 * ab
        if x < 0:
            continue
        x_sqrt = round(x ** 0.5)
        if x_sqrt ** 2 != x:
            continue
        # a + b = c, a - b = x_sqrt
        res = max(res, ab * c)
    table[n] = res

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((table[n]))
