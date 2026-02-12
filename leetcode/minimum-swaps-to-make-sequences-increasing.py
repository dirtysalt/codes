#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        inf = (1 << 30)
        dp = [[inf] * n, [inf] * n]
        dp[0][0] = 0
        dp[1][0] = 1

        for i in range(1, n):
            t0, t1 = inf, inf
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                t0 = min(t0, dp[0][i - 1])
                t1 = min(t1, dp[1][i - 1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                t0 = min(t0, dp[1][i - 1])
                t1 = min(t1, dp[0][i - 1] + 1)

            dp[0][i] = t0
            dp[1][i] = t1

        ans = min(dp[0][-1], dp[1][-1])
        return ans
