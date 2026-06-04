#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        idx = 0
        for i in range(n):
            if nums[i] != 0:
                nums[idx] = nums[i]
                idx += 1
        for i in range(idx, n):
            nums[i] = 0
