#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        for x in reversed(nums):
            left = total - x
            if left > x:
                return left + x
            total -= x
        return -1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 5, 5], 15),
    ([1, 12, 1, 2, 5, 50, 3], 12),
    ([5, 5, 50], -1),
]

aatest_helper.run_test_cases(Solution().largestPerimeter, cases)

if __name__ == '__main__':
    pass
