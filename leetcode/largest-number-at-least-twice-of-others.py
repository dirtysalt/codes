#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xs = list(enumerate(nums))
        xs.sort(key=lambda x: x[1])
        if len(xs) <= 1:
            return 0
        if xs[-1][1] >= 2 * xs[-2][1]:
            return xs[-1][0]
        return -1
