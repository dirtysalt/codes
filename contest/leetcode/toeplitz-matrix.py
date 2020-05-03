#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        n = len(matrix)
        m = len(matrix[0])
        for (x, y) in [(r, 0) for r in range(n)] + [(0, c) for c in range(m)]:
            val = matrix[x][y]
            while x < n and y < m:
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
        return True
