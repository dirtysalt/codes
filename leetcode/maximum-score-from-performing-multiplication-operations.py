#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        m = len(multipliers)
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for k in range(1, m + 1):
            for i in range(k + 1):
                # dp[k][i] = dp[k-1][i-1] + mul[k-1] * nums[i-1]
                # dp[k-1][i] + mul[k-1] * nums[j]
                res = - (1 << 30)
                if i != 0:
                    a = dp[k - 1][i - 1] + multipliers[k - 1] * nums[i - 1]
                    res = max(res, a)
                if i != k:
                    a = dp[k - 1][i] + multipliers[k - 1] * nums[n - k + i]
                    res = max(res, a)
                dp[k][i] = res

        ans = max(dp[m])
        return ans


cases = [
    ([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6], 102),
    ([1, 2, 3], [3, 2, 1], 14),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumScore, cases)
