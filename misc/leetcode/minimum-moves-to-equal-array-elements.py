#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_num = min(nums)
        res = 0
        for x in nums:
            res += (x - min_num)
        return res
