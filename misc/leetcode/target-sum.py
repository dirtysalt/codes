#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1

        for x in nums:
            dp2 = defaultdict(int)
            for k, v in dp.items():
                dp2[k + x] += v
                dp2[k - x] += v
            dp = dp2
            # print(dp)


        ans = dp[S]
        return ans


cases = [
    ([1, 1, 1, 1, 1], 3, 5)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().findTargetSumWays, cases)
