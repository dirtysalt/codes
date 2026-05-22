#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        for i in range(n - 1):
            for j in range(m - 1):
                b = 0
                for dx, dy in ((0, 1), (0, 0), (1, 0), (1, 1)):
                    if grid[i + dx][j + dy] == 'B':
                        b += 1
                if b <= 1 or b >= 3:
                    return True
        return False

