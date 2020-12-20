#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4: return 0
        nums.sort()

        ans = 1 << 61
        for i in range(3 + 1):
            j = 3 - i
            a = nums[i]
            b = nums[-(j + 1)]
            ans = min(ans, b - a)
        return ans


cases = [
    ([5, 3, 2, 4], 0),
    ([1, 5, 0, 10, 14], 1),
    ([6, 6, 0, 1, 1, 4, 6], 2),
    ([1, 5, 6, 14, 15], 1),
    ([82, 81, 95, 75, 20], 1),
    ([20, 66, 68, 57, 45, 18, 42, 34, 37, 58], 31),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDifference, cases)
