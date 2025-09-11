#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin

n = int(fh.readline())
c = list(map(int, fh.readline().strip().split(' ')))

dp = [0] * n

for i in range(1, n):
    if c[i] == 1:
        dp[i] = 1 << 31
    elif i == 1:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = min(dp[i - 1], dp[i - 2]) + 1

print((dp[n - 1]))
