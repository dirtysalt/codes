#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return sum(set([n for n in nums if n >= 0])) if max(nums) >= 0 else max(nums)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 5], 15),
    ([1, 1, 0, 1, 1], 1),
    ([1, 2, -1, -2, 1, 0, -1], 3),
    ([4, 3, 4, 8], 15),
    ([-6, 12, 20, 20, -14, 10, -12], 42),
]

aatest_helper.run_test_cases(Solution().maxSum, cases)

if __name__ == '__main__':
    pass
