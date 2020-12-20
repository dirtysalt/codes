#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         r = set()
#         c = set()
#         n = len(matrix)
#         m = len(matrix[0])
#
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     r.add(i)
#                     c.add(j)
#
#         for i in r:
#             for j in range(m):
#                 matrix[i][j] = 0
#         for j in c:
#             for i in range(n):
#                 matrix[i][j] = 0


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None
        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
