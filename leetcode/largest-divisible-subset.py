#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        nums.sort()
        dp = [1] * n
        back = [-1] * n
        max_idx = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0:
                    if dp[j] < (dp[i] + 1):
                        dp[j] = dp[i] + 1
                        back[j] = i
                        if dp[j] > dp[max_idx]:
                            max_idx = j

        ans = []
        while max_idx != -1:
            ans.append(nums[max_idx])
            max_idx = back[max_idx]
        ans.sort()
        return ans


import aatest_helper

cases = [
    ([1, 2, 3], [1, 2]),
    ([1, 2, 4, 8], [1, 2, 4, 8])
]

aatest_helper.run_test_cases(Solution().largestDivisibleSubset, cases)
