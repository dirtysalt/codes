#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)

        def diag(i, j):
            return i == j or i == (n - 1 - j)

        for i in range(n):
            for j in range(n):
                if diag(i, j) == (grid[i][j] == 0):
                    return False

        return True


if __name__ == '__main__':
    pass
