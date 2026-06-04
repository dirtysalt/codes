#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(vals, wts, n, W):
    dp = []
    dp.append([0] * (W + 1))
    dp.append([0] * (W + 1))
    now = 0
    for i in range(n):
        val = vals[i]
        wt = wts[i]
        for w in range(0, W + 1):
            dp[1 - now][w] = dp[now][w]
        for w in range(0, W + 1 - wt):
            dp[1 - now][w + wt] = max(dp[1 - now][w + wt], dp[now][w] + val)
        now = 1 - now
    return max(dp[now])


t = int(input())
for _ in range(t):
    n = int(input())
    W = int(input())
    vals = [int(x) for x in input().rstrip().split()]
    ws = [int(x) for x in input().rstrip().split()]
    print(solve(vals, ws, n, W))
