#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        if not n: return False
        m = len(matrix[0])
        if not m: return False

        r, c = 0, m - 1
        while r < n and c >= 0:
            v = matrix[r][c]
            if v == target:
                return True
            elif v > target:
                c -= 1
            else:
                r += 1
        return False
