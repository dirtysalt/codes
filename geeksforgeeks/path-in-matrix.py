#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid, n):
    dp = []
    dp.append([0] * n)
    dp.append([0] * n)
    now = 0
    for i in range(n):
        for j in range(n):
            res = dp[now][j]
            if j > 0:
                res = max(res, dp[now][j - 1])
            if j < n - 1:
                res = max(res, dp[now][j + 1])
            dp[1 - now][j] = grid[i * n + j] + res
        now = 1 - now
        # print(dp[now])
    return max(dp[now])


t = int(input())
for _ in range(t):
    n = int(input())
    grid = [int(x) for x in input().rstrip().split()]
    # import numpy as np
    #
    # grid2 = np.array(grid).reshape((n, n))
    # print(grid2)
    print(solve(grid, n))
