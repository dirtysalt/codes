#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(A)
        m = len(A[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][n - j - 1] = 1 - A[i][j]
        return ans
