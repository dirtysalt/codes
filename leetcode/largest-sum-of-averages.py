#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        ninf = -(1 << 30)
        dp = [[ninf] * (K + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for k in range(1, K + 1):
                acc = 0
                ans = 0
                for j in reversed(range(1, i + 1)):
                    acc += A[j - 1]
                    sz = (i - j + 1)
                    avg = acc / sz
                    ans = max(ans, avg + dp[j - 1][k - 1])
                dp[i][k] = ans
        ans = dp[n][k]
        return ans
