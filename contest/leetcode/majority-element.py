#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        value = nums[0]
        count = 1
        for i in range(1, n):
            if count == 0:
                value = nums[i]
                count = 1
            elif value == nums[i]:
                count += 1
            else:
                count -= 1
        return value

