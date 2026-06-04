#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        n, m = len(grid), len(grid[0])

        visited = set()

        def dfs(i, j):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '1' and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)

        c = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    c += 1
        return c
