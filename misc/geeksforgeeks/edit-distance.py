#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = []
    dp.append([0] * (m + 1))
    dp.append([0] * (m + 1))
    now = 0
    for j in range(0, m + 1):
        dp[now][j] = j

    for i in range(1, n + 1):
        dp[1 - now][0] = i
        for j in range(1, m + 1):
            # s1[i-1] vs s2[j-1]
            res = 1 << 31
            res = min(res, dp[now][j] + 1)
            res = min(res, dp[1 - now][j - 1] + 1)
            res = min(res, dp[now][j - 1] + 1)
            if s1[i - 1] == s2[j - 1]:
                res = min(res, dp[now][j - 1])
            dp[1 - now][j] = res
        now = 1 - now
    return dp[now][m]


t = int(input())
for _ in range(t):
    input()
    s1, s2 = input().rstrip().split()
    print(solve(s1, s2))
