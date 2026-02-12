#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def rev(a, i, j):
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        n = len(nums)
        k = k % n
        if k == 0:
            return

        rev(nums, 0, n - k - 1)
        rev(nums, n - k, n - 1)
        rev(nums, 0, n - 1)
