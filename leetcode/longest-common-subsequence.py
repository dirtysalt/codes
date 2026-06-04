#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                res = max(dp[i][j - 1], dp[i - 1][j])
                if text1[i - 1] == text2[j - 1]:
                    res = max(res, dp[i - 1][j - 1] + 1)
                dp[i][j] = res
        ans = dp[-1][-1]
        return ans
