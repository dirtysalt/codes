#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visit = set()

        def dfs(x, y):
            visit.add((x, y))
            c = grid[x][y]
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] > 0 and (x2, y2) not in visit:
                    c += dfs(x2, y2)
            return c

        ans = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in visit or grid[i][j] == 0:
                    continue
                c = dfs(i, j)
                ans = max(ans, c)
        return ans


if __name__ == '__main__':
    pass
