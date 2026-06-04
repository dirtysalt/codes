#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def prime_build_table(n):
    table = [1] * (n + 1)
    table[1] = 0
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        if table[i] == 0:
            continue
        for j in range(2, n // i + 1):
            table[i * j] = 0
    return table


def prime_upper_bound(n):
    return min(n - 1, round(n ** 0.5) + 2)


N = 10 ** 6
prime_table = prime_build_table(N)
table = [0] * (N + 1)
table[1] = 0
table[2] = 2
res = 2
for n in range(3, N + 1):
    if prime_table[n]:
        res += n
    table[n] = res

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((table[n]))
