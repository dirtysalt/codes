#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(triangle):
    n = len(triangle)
    dp = [[0] * n, [0] * n]
    now = 0
    dp[now][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(0, i + 1):
            res = -1
            if j > 0:
                res = max(res, dp[now][j - 1])
            if j < i:
                res = max(res, dp[now][j])
            res += triangle[i][j]
            dp[1 - now][j] = res
        now = 1 - now
    return max(dp[now])


t = int(input())
for _ in range(t):
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append([int(x) for x in input().rstrip().split()])
    print((solve(triangle)))
