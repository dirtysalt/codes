#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [None] * (target + 1)
        dp[0] = ""

        def str_max(a, b):
            if a is None:
                return b
            if b is None:
                return a
            if len(a) > len(b):
                return a
            elif len(a) < len(b):
                return b
            return max(a, b)

        for i in range(target):
            if dp[i] is None: continue
            for j in range(len(cost)):
                t = i + cost[j]
                if t <= target:
                    a = dp[i] + str(j + 1)
                    b = str(j + 1) + dp[i]
                    dp[t] = str_max(dp[t], str_max(a, b))

        ans = dp[target]
        if ans is None:
            ans = "0"
        return ans


cases = [
    ([4, 3, 2, 5, 6, 7, 2, 5, 5], 9, "7772"),
    ([6, 10, 15, 40, 40, 40, 40, 40, 40], 47, "32211"),
    ([2, 4, 6, 2, 4, 6, 4, 4, 4], 5, "0"),
    ([7, 6, 5, 5, 5, 6, 8, 7, 8], 12, "85"),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1], 5000, "9" * 5000),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().largestNumber, cases)
