#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        inf = 1 << 30

        dp = [[inf] * 100, [inf] * 100]
        for i in range(len(A[0])):
            dp[0][i] = A[0][i]

        now = 0
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                t = inf
                for dx in (-1, 0, 1):
                    if 0 <= (j + dx) < len(A[i - 1]):
                        res = dp[now][j + dx] + A[i][j]
                        t = min(res, t)
                dp[1 - now][j] = t
            now = 1 - now

        ans = min(dp[now])
        return ans


cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().minFallingPathSum, cases)
