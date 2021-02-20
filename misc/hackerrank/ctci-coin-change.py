#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def make_change(coins, n):
    m = len(coins)
    dp = []
    for i in range(n + 1):
        dp.append([0] * (m + 1))

    # init.
    for i in range(n + 1):
        dp[i][m] = 1
    for i in range(m + 1):
        dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = coins[j - 1]
            value = dp[i][j - 1]
            if i >= c:
                value += dp[i - c][j]
            dp[i][j] = value
    return dp[n][m]


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print((make_change(coins, n)))
