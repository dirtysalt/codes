#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        for i in range(n):
            while nums[i] != (i + 1):
                x = nums[i]
                y = nums[x - 1]
                if y == x:
                    break
                nums[i], nums[x - 1] = nums[x - 1], nums[i]

        ans = []
        for i in range(n):
            if nums[i] != (i + 1):
                ans.append(nums[i])
        return ans
