#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        inf = (1 << 30)
        k = 3
        dp = [inf] * k

        for x in nums:
            for i in reversed(range(k)):
                if (i == 0 or x > dp[i - 1]) and x < dp[i]:
                    dp[i] = x
        print(dp)
        ans = (dp[-1] != inf)
        return ans


cases = [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().increasingTriplet, cases)
