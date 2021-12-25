#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        visited = set()

        def dfs(i, j):
            if (i, j) in visited:
                return 0

            ans = 4
            visited.add((i, j))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i + dx, j + dy
                if 0 <= i2 < n and 0 <= j2 < m and grid[i2][j2]:
                    ans -= 1
                    ans += dfs(i2, j2)
            return ans

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i, j)
        return 0


true, false, null = True, False, None
cases = [
    ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
    ([[1, 0]], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().islandPerimeter, cases)

if __name__ == '__main__':
    pass
