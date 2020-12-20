#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        # dp[i][d] # 以A[i]截止，差距为d的最长序列长度
        dp = [{}]
        ans = 0
        for i in range(1, n):
            dp.append({})
            for j in range(i):
                d = A[i] - A[j]
                value = dp[j].get(d, 1) + 1
                dp[i][d] = value
                ans = max(ans, value)
        return ans


cases = [
    (
        [44, 46, 22, 68, 45, 66, 43, 9, 37, 30, 50, 67, 32, 47, 44, 11, 15, 4, 11, 6, 20, 64, 54, 54, 61, 63, 23, 43, 3,
         12, 51, 61, 16, 57, 14, 12, 55, 17, 18, 25, 19, 28, 45, 56, 29, 39, 52, 8, 1, 21, 17, 21, 23, 70, 51, 61, 21,
         52,
         25, 28], 6),
    (
        [61, 28, 67, 53, 13, 6, 70, 5, 79, 82, 60, 60, 84, 17, 80, 25, 82, 82, 69, 76, 81, 43, 58, 86, 18, 78, 4, 25, 8,
         30,
         33, 87, 91, 18, 90, 26, 62, 11, 28, 66, 9, 33, 58, 66, 47, 48, 80, 38, 25, 57, 4, 84, 79, 71, 54, 84, 63, 32,
         97,
         62, 26, 68, 5, 69, 54, 93, 25, 26, 100, 73, 24, 94, 80, 39, 30, 45, 95, 80, 0, 29, 57, 98, 92, 15, 17, 76, 69,
         11,
         57, 56, 48, 10, 28, 7, 63, 66, 53, 58, 12, 58], 6)

]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestArithSeqLength, cases)
