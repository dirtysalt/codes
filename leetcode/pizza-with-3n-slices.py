#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def calc(xs):
            n = len(xs)
            t = (n + 1) // 3
            dp = [[0] * (t + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, t + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i >= 2 else 0) + xs[i - 1])
            return dp[n][t]

        ans0 = calc(slices[:-1])
        ans1 = calc(slices[1:])
        ans = max(ans0, ans1)
        return ans


cases = [
    ([1, 2, 3, 4, 5, 6], 10),
    ([8, 9, 8, 6, 1, 1], 16),
    ([4, 1, 2, 5, 8, 3, 1, 9, 7], 21),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSizeSlices, cases)
