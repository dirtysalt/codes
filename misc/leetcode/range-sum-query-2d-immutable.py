#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n, self.m = 0, 0
        if not matrix:
            return

        n, m = len(matrix), len(matrix[0])
        self.n, self.m = n, m
        acc = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                acc[i + 1][j + 1] = acc[i + 1][j] + matrix[i][j]
            for j in range(m):
                acc[i + 1][j + 1] += acc[i][j + 1]
        self.acc = acc

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        n, m = self.n, self.m
        if row1 < 0 or row1 >= n or row2 < 0 or row2 >= n:
            return 0
        if col1 < 0 or col1 >= m or col2 < 0 or col2 >= m:
            return 0

        acc = self.acc
        ans = acc[row2 + 1][col2 + 1] - acc[row2 + 1][col1] - acc[row1][col2 + 1] + acc[row1][col1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
