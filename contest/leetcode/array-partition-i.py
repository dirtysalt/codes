#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(0, n, 2):
            ans += min(nums[i], nums[i + 1])
        return ans
