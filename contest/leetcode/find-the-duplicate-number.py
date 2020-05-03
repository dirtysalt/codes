#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        def check(x):
            low, high, eq = 0, 0, 0
            for v in nums:
                if v < x:
                    low += 1
                elif v == x:
                    eq += 1
                elif v > x:
                    high += 1
            if eq >= 2:
                return 0
            elif low > (x - 1):
                return -1
            else:
                return 1

        s, e = 1, n - 1
        while s < e:
            m = (s + e) // 2
            res = check(m)
            if res == 0:
                return m
            elif res == -1:
                e = m - 1
            else:
                s = m + 1
        return s
