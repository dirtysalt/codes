#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         import functools
#         return list(map(list, functools.permutation(nums)))


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        def f(nums, idx):
            if idx == len(nums):
                res.append(list(nums))
                return
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                f(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        f(nums, 0)
        return res
