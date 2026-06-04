#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            ans = 0
            for j in range(i):
                k = i - j - 1
                ans += dp[j] * dp[k]
            dp[i] = ans

        ans = dp[n]
        return ans
