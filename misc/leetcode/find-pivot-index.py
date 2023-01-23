#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xsum = sum(nums)
        acc = 0
        for i in range(len(nums)):
            if acc == (xsum - acc - nums[i]):
                return i
            acc += nums[i]
        return -1
