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


def solve(n):
    ub = prime_upper_bound(n)
    table = prime_build_table(ub)
    last_prime = None
    for p in range(2, ub + 1):
        if not table[p]:
            continue
        if n % p == 0:
            last_prime = p
            while n % p == 0:
                n = n // p
    last_prime = n if not last_prime else max(last_prime, n)
    return last_prime


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((solve(n)))
