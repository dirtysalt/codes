#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n):
    dp = [0] * (3 + n)
    dp[0] = 1
    for i in range(0, n):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
        dp[i + 3] += dp[i]
    return dp[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
