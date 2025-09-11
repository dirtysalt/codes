#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class neighborSum:

    def __init__(self, grid: List[List[int]]):
        n, m = len(grid), len(grid[0])
        self.n, self.m = n, m
        self.grid = grid
        self.idx = {}
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                self.idx[v] = (i, j)

    def adjacentSum(self, value: int) -> int:
        i, j = self.idx[value]
        n, m = self.n, self.m
        grid = self.grid
        ans = 0
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m:
                ans += grid[x][y]
        return ans

    def diagonalSum(self, value: int) -> int:
        i, j = self.idx[value]
        n, m = self.n, self.m
        grid = self.grid
        ans = 0
        for dx, dy in ((-1, 1), (-1, -1), (1, 1), (1, -1)):
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m:
                ans += grid[x][y]
        return ans


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)

if __name__ == '__main__':
    pass
