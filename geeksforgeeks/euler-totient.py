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


table = prime_build_table(10 ** 6)
primes = [x for x in range(len(table)) if table[x] and x > 1]


def solve(n):
    res = 1
    for p in primes:
        if (res * p) > n:
            break
        res *= p
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
