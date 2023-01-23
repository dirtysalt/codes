#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        matched = 0
        res = None
        for i in range(self.n):
            if self.nums[i] == target:
                matched += 1
                if random.randint(0, matched - 1) == 0:
                    res = i
        assert res is not None
        return res

