#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if r == 0 or c == 0: return nums
        n = len(nums)
        m = len(nums[0])
        if (n * m) != (r * c): return nums

        ans = []
        row = []
        for i in range(n):
            for j in range(m):
                v = nums[i][j]
                row.append(v)
                if len(row) % c == 0:
                    ans.append(row)
                    row = []
        return ans
