#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def test(G):
            mark = set()
            C = 0

            def visit(x, y):
                mark.add((x, y))
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < n and 0 <= y2 < m and G[x2][y2] == 1 and (x2, y2) not in mark:
                        visit(x2, y2)

            for i in range(n):
                for j in range(m):
                    if G[i][j] == 1 and (i, j) not in mark:
                        C += 1
                        visit(i, j)

            return C

        if test(grid) > 1: return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if test(grid) > 1:
                        return 1
                    grid[i][j] = 1

        return 2


cases = [
    ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 2),
    ([[1, 1]], 2),
    ([[1, 0, 1, 0]], 0),
    ([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]], 1),
    ([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]], 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDays, cases)
