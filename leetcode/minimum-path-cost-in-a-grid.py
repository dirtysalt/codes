#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        costs = [[0] * m for _ in range(2)]
        now = 0
        for j in range(m):
            costs[0][j] = grid[0][j]

        inf = 1 << 30
        for i in range(n - 1):
            for j in range(m):
                costs[1 - now][j] = inf

            for j in range(m):
                value = grid[i][j]
                for k in range(m):
                    c = moveCost[value][k]
                    costs[1 - now][k] = min(costs[1 - now][k], costs[now][j] + c + grid[i + 1][k])

            now = 1 - now

        ans = min(costs[now])
        return ans


true, false, null = True, False, None
cases = [
    ([[5, 3], [4, 0], [2, 1]], [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]], 17),
    ([[5, 1, 2], [4, 0, 3]], [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]], 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minPathCost, cases)

if __name__ == '__main__':
    pass
