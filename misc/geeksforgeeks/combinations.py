#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, r):
    if r > n:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    MOD = 10 ** 9 + 7
    for i in range(1, n + 1):
        for j in range(min(i, r), -1, -1):
            dp[j] = (dp[j - 1] + dp[j]) % MOD
    return dp[r]


t = int(input())
for _ in range(t):
    n, r = [int(x) for x in input().rstrip().split()]
    print(solve(n, r))
