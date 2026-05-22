#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        ans = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                t = 0
                for k in (-1, 0, 1):
                    t += grid[i - 1][k + j]
                    t += grid[i + 1][k + j]
                t += grid[i][j]
                ans = max(ans, t)
        return ans


if __name__ == '__main__':
    pass
