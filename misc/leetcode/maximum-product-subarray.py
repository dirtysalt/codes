#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        ans = nums[0]
        x, y = 1, 1
        for i in range(n):
            a, b = x * nums[i], y * nums[i]
            x = min(a, b, nums[i])
            y = max(a, b, nums[i])
            ans = max(ans, y)
        return ans


cases = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([3, -1, 4], 4),
    ([-4, -3, -2], 12)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProduct, cases)
