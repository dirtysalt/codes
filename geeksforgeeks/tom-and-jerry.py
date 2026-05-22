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


def factor_build_table(n):
    table = []
    for i in range(n + 1):
        table.append([])
    res = 0
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        for j in range(i, n // i + 1):
            v = i * j
            table[v].append(i)
            res += 1
    return table


N = 10 ** 6

# factor_table = factor_build_table(N)

# dp = [0] * (N + 1)
# dp[1] = 0
# for x in range(2, N + 1):
#     if dp[x - 1] == 0:
#         dp[x] = 1
#         continue
#     ok = 0
#     for f in factor_table[x]:
#         f2 = x // f
#         if dp[x - f] == 0 or dp[x - f2] == 0:
#             ok = 1
#             break
#     dp[x] = ok
#
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(dp[n])

prime_table = prime_build_table(N)


def solve(n):
    dp = [0] * (n + 1)
    dp[1] = 0
    for x in range(2, n + 1):
        if dp[x - 1] == 0:
            dp[x] = 1
            continue
        if prime_table[x]:
            continue
        ok = 0
        for f in range(2, prime_upper_bound(x)):
            if x % f != 0:
                continue
            f2 = x // f
            if dp[x - f] == 0 or dp[x - f2] == 0:
                ok = 1
                break
        dp[x] = ok
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
