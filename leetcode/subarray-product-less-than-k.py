#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start = 0
        acc = 1
        ans = 0
        for i in range(len(nums)):
            acc *= nums[i]
            while acc >= k and start <= i:
                acc //= nums[start]
                start += 1
            ans += (i - start + 1)
        return ans
