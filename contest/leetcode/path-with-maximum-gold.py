#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            res = grid[i][j]
            grid[i][j] = 0

            max_tmp = 0
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != 0:
                    tmp = dfs(x, y)
                    max_tmp = max(max_tmp, tmp)

            grid[i][j] = res
            res += max_tmp
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    res = dfs(i, j)
                    ans = max(res, ans)
        return ans


cases = [
    ([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().getMaximumGold, cases)
