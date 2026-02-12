#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row, col = [], []
        for i in range(n):
            row.append(grid[i].copy())
            col.append(grid[i].copy())

        for i in range(n):
            for j in range(1, m):
                row[i][j] += row[i][j - 1]
        for i in range(m):
            for j in range(1, n):
                col[j][i] += col[j - 1][i]

        # print(grid, row, col)
        size = min(n, m)
        for sz in reversed(range(size + 1)):
            for i in range(n):
                if (i + sz - 1) >= n: break
                for j in range(m):
                    if (j + sz - 1) >= m: break
                    a = row[i][j + sz - 1] - (row[i][j - 1] if j > 0 else 0)
                    b = row[i + sz - 1][j + sz - 1] - (row[i + sz - 1][j - 1] if j > 0 else 0)
                    c = col[i + sz - 1][j] - (col[i - 1][j] if i > 0 else 0)
                    d = col[i + sz - 1][j + sz - 1] - (col[i - 1][j + sz - 1] if i > 0 else 0)
                    # print(a, b, c, d, sz)
                    if a == b == c == d == sz:
                        return sz * sz
        return 0


cases = [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largest1BorderedSquare, cases)
