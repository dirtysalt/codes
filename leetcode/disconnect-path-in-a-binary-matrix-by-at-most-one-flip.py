#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])

        def search():
            dp = [[0] * m for _ in range(n)]
            dp[-1][-1] = 1
            for i in reversed(range(n)):
                for j in reversed(range(m)):
                    if grid[i][j] == 0: continue
                    if (i + 1) < n and dp[i + 1][j] == 1:
                        dp[i][j] = 1
                    if (j + 1) < m and dp[i][j + 1] == 1:
                        dp[i][j] = 1

            if dp[0][0] == 0: return []
            path = [(0, 0)]
            while True:
                (i, j) = path[-1]
                if (i, j) == (n - 1, m - 1): break
                if (i + 1) < n and dp[i + 1][j] == 1:
                    path.append((i + 1, j))
                    continue
                if (j + 1) < m and dp[i][j + 1] == 1:
                    path.append((i, j + 1))
                    continue
            return path

        path = search()
        # print(path)
        if not path: return True
        for x, y in path[1:-1]:
            grid[x][y] = 0
        # print(grid)
        path = search()
        if not path: return True
        return False


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1, 1], [1, 0, 0], [1, 1, 1]], true),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], false),
    ([[1, 1, 1]], true),
    ([[1, 0, 0], [1, 1, 1]], true)
]

aatest_helper.run_test_cases(Solution().isPossibleToCutPath, cases)

if __name__ == '__main__':
    pass
