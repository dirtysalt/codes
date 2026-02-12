#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        r0, r1, c0, c1 = n - 1, 0, m - 1, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    r0 = min(r0, i)
                    r1 = max(r1, i)
                    c0 = min(c0, j)
                    c1 = max(c1, j)

        ans = (r1 - r0 + 1) * (c1 - c0 + 1)
        return ans


if __name__ == '__main__':
    pass
