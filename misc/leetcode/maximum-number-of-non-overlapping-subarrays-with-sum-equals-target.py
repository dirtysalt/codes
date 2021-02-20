#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ps = {}
        n = len(nums)
        dp = [0] * (n + 1)
        ps[0] = -1

        acc = 0
        for i in range(n):
            x = nums[i]
            acc += x
            exp = acc - target
            value = dp[i - 1]
            if exp in ps:
                p = ps[exp]
                value = max(value, dp[p] + 1)
            dp[i] = value
            ps[acc] = i
        ans = dp[n - 1]
        return ans


cases = [
    ([1, 1, 1, 1, 1], 2, 2),
    ([-1, 3, 5, 1, 4, 2, -9], 6, 2),
    ([-2, 6, 6, 3, 5, 4, 1, 2, 8], 10, 3),
    ([0, 0, 0], 0, 3),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maxNonOverlapping, cases)
