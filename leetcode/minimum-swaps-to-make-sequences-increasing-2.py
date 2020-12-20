#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[0, 0], [0, 0]]
        k = 0
        dp[0][1] = 1
        inf = 1 << 20
        for i in range(1, n):
            a, b = inf, inf
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                a = min(a, dp[k][0])
                b = min(b, dp[k][1] + 1)

            if B[i - 1] < A[i] and A[i - 1] < B[i]:
                a = min(a, dp[k][1])
                b = min(b, dp[k][0] + 1)

            dp[1 - k][0] = a
            dp[1 - k][1] = b
            k = 1 - k

        ans = min(dp[k])
        return ans


cases = [
    ([1, 3, 5, 4], [1, 2, 3, 7], 1),
    ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9], 1),
    ([3, 3, 8, 9, 10], [1, 7, 4, 6, 8], 1),
    ([0, 7, 8, 10, 10, 11, 12, 13, 19, 18], [4, 4, 5, 7, 11, 14, 15, 16, 17, 20], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSwap, cases)
