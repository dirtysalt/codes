#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(xs):
    dp = [[0] * 32, [0] * 32]
    for x in xs:
        for i in range(0, 32):
            c = (x >> i) & 0x1
            dp[c][i] += 1
    res = 0
    for i in range(32):
        res += 2 * dp[0][i] * dp[1][i]
    MOD = 10 ** 9 + 7
    return res % MOD


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
