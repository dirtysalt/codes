#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import aatest_helper

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0:
            return m
        elif m == 0:
            return n

        dp = []
        inf = (1 << 30)
        for i in range(n+1):
            dp.append([inf] * (m+1))

        for i in range(m+1):
            dp[0][i] = i
        for i in range(n+1):
            dp[i][0] = i

        for i in range(n):
            for j in range(m):
                # dp[i+1][j+1], w1[i], w2[j]
                res = min(dp[i+1][j], dp[i][j+1]) + 1
                if word1[i] == word2[j]:
                    res = min(res, dp[i][j])
                dp[i+1][j+1] = res
        
        return dp[n][m]

cases = [
    ("sea", "ea", 1),
    ("sea", "eat", 2)
]
aatest_helper.run_test_cases(Solution().minDistance, cases)

