#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# dp[i] 表示最大值是 xs[i] LIS长度
def solve(xs):
    n = len(xs)
    if n == 0: return 0
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        res = 0
        for j in range(0, i):
            if xs[i] > xs[j]:
                res = max(res, dp[j])
        res += 1
        dp[i] = res
    return max(dp)


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    assert n == len(xs)
    print(solve(xs))
