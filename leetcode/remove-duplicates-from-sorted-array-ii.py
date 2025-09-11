#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0

        for x in nums:
            if j >= 2 and x == nums[j - 1] == nums[j - 2]:
                continue
            nums[j] = x
            j += 1

        return j


cases = [
    ([1, 1, 1, 2, 2, 3], 5),
    ([1, 1, 1, 2], 3),
    ([1], 1)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().removeDuplicates, cases)
