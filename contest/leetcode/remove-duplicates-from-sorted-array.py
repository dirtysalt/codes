#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from leetcode import aatest_helper


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = None
        k = 0
        for v in nums:
            if v == prev:
                continue
            nums[k] = v
            k += 1
            prev = v
        return k


cases = [
    ([1, 1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
]
sol = Solution()
aatest_helper.run_test_cases(sol.removeDuplicates, cases)
