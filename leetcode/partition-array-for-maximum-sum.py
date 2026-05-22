#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = {}

        def fun(i):
            if i < 0:
                return 0

            if i in dp:
                return dp[i]

            ans = 0
            max_value = A[i]
            for sz in range(1, K + 1):
                if (i - sz + 1) < 0:
                    break
                max_value = max(max_value, A[i - sz + 1])
                ans = max(ans, max_value * sz + fun(i - sz))

            dp[i] = ans
            return ans

        ans = fun(len(A) - 1)
        return ans
