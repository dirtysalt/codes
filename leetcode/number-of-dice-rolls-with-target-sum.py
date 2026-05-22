#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = {}
        MOD = 10 ** 9 + 7

        def fun(d, t):
            if d == 0:
                return 1 if t == 0 else 0

            key = (d, t)
            if key in dp:
                return dp[key]

            ans = 0
            for x in range(1, f + 1):
                if t >= x:
                    ans += fun(d - 1, t - x)
            ans = ans % MOD
            dp[key] = ans
            return ans

        ans = fun(d, target)
        return ans
