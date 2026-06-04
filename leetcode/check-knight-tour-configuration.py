#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        step = [0] * (n * m)
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                step[v] = (i, j)

        if step[0] != (0, 0): return False
        for i in range(1, n * m):
            x2, y2 = step[i]
            x, y = step[i - 1]
            d = abs(x - x2)
            d2 = abs(y - y2)
            if (d == 2 and d2 == 1) or (d == 1 and d2 == 2):
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    pass
