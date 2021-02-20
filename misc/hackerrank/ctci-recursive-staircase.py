#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n):
    dp = [0] * (n + 4)
    dp[0] = 1
    for i in range(0, n + 1):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
        dp[i + 3] += dp[i]
    print((dp[n]))


cases = int(input())
for _ in range(cases):
    n = int(input())
    solve(n)
