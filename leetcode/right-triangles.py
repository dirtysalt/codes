#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row = [0] * n
        for i in range(n):
            for j in range(m):
                row[i] += grid[i][j]

        ans = 0
        for j in range(m):
            c = 0
            for i in range(n):
                c += grid[i][j]

            for i in range(n):
                if grid[i][j]:
                    ans += (c - 1) * (row[i] - 1)

        return ans


if __name__ == '__main__':
    pass
