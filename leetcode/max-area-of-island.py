#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        def dfs(xy):
            x, y = xy
            cnt = 1
            grid[x][y] |= 2
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1:
                    cnt += dfs((x2, y2))
            return cnt

        ans = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    res = dfs((x, y))
                    ans = max(ans, res)

        return ans
