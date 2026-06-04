#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [0] * n
        cols = [0] * m

        for i in range(n):
            x = max(grid[i])
            rows[i] = x
        for i in range(m):
            x = max((grid[j][i] for j in range(n)))
            cols[i] = x

        ans = 0
        for i in range(n):
            for j in range(m):
                h = min(rows[i], cols[j])
                ans += (h - grid[i][j])
        return ans
