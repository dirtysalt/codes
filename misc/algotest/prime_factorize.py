#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 100000
factor = [0] * (N + 1)
for i in range(2, N + 1):
    if factor[i] != 0: continue
    for j in range(1, N // i + 1):
        factor[i * j] = i


def factorize(x):
    ans = []
    while factor[x] != 0:
        f = factor[x]
        c = 0
        while x % f == 0:
            x = x // f
            c += 1
        ans.append((f, c))
    return ans


def validate(x, fcs):
    ans = 1
    for f, c in fcs:
        ans = pow(f, c) * ans
    return ans == x


for x in range(1, N + 1):
    fcs = factorize(x)
    if not validate(x, fcs):
        print(x, fcs)

print(factorize(N))
