#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        for j in range(m):
            exp = grid[0][j] + 1
            for i in range(1, n):
                diff = exp - grid[i][j]
                exp = max(exp, grid[i][j]) + 1
                ans += max(diff, 0)
        return ans


if __name__ == '__main__':
    pass
