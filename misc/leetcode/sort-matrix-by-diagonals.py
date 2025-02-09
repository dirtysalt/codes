#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            r, c = i, 0
            pos = []
            while r < n and c < n:
                pos.append((r, c))
                r, c = r + 1, c + 1
            values = [grid[r][c] for r, c in pos]
            values.sort(reverse=True)
            for i, (r, c) in enumerate(pos):
                grid[r][c] = values[i]

        for j in range(1, n):
            r, c = 0, j
            pos = []
            while r < n and c < n:
                pos.append((r, c))
                r, c = r + 1, c + 1
            values = [grid[r][c] for r, c in pos]
            values.sort()
            for i, (r, c) in enumerate(pos):
                grid[r][c] = values[i]

        return grid

if __name__ == '__main__':
    pass
