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


table = prime_build_table(prime_upper_bound(10 ** 9))
primes = [x for x in range(2, len(table)) if table[x]]


def solve(l, r):
    MOD = 10 ** 9 + 7
    # res = 1
    # for i in range(l, r + 1):
    #     if table[i]:
    #         print(i)
    #         res *= i
    # print(res % MOD)

    n = (r - l + 1)
    dp = [1] * n
    for p in primes:
        x = (l + p - 1) // p * p
        if x <= p:
            assert (x == 0 or x == p)
            x += p
        while x <= r:
            # print('mark {}'.format(x))
            dp[x - l] = 0
            x += p
    res = 1
    for i in range(n):
        x = l + i
        if dp[i]:
            res *= x
            res %= MOD
    return res


t = int(input())
for _ in range(t):
    l, r = [int(x) for x in input().rstrip().split()]
    print(solve(l, r))
