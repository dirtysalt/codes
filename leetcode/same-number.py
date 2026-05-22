#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """

    def sameNumber(self, nums, k):
        # Write your code here

        bk = dict()
        for i in range(0, len(nums)):
            v = nums[i]
            last = bk.get(v)
            if last is not None and (i - last) < k:
                return 'YES'
            bk[v] = i
        return 'NO'
