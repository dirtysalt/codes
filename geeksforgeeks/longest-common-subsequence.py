#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (m + 1))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    return dp[n][m]


def solve_rolling(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = []
    dp.append([0] * (m + 1))
    dp.append([0] * (m + 1))
    now = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[now][j] = max(dp[1 - now][j], dp[now][j - 1])
            if s1[i - 1] == s2[j - 1]:
                dp[now][j] = max(dp[now][j], dp[1 - now][j - 1] + 1)
        now = 1 - now
    return dp[1 - now][m]


t = int(input())
for _ in range(t):
    input()
    s1 = input().rstrip()
    s2 = input().rstrip()
    print(solve_rolling(s1, s2))
