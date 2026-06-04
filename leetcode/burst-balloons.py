#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# 这个状态方程是，dp[s..e] 戳破所有除s,e之外的气球可以获得的最大值
# = max(dp[s..i] + dp[i..e] + x[i] * x[s] * x[e])
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = {}

        def run(s, e):
            if (s + 1) == e:
                return 0

            key = '{}.{}'.format(s, e)
            if key in dp:
                return dp[key]

            res = 0
            for i in range(s + 1, e):
                x = run(s, i) + run(i, e) + nums[s] * nums[i] * nums[e]
                res = max(res, x)

            dp[key] = res
            return res

        ans = run(0, n - 1)
        return ans


cases = [
    ([3, 1, 5, 8], 167),
    ([], 0),
    ([9], 9),
    ([1, 2], 4),
    ([1, 2, 3], 12),
    ([35, 16, 83, 87, 84, 59, 48, 41], 1583373),
    ([35, 16, 83, 87, 84], 900088),
    ([3, 1, 8, 8, 8], 760)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maxCoins, cases)
