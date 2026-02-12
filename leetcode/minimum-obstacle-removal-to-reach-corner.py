#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        INF = 1 << 30
        cost = [[INF] * m for _ in range(n)]
        import heapq
        Q = [(0, 0, 0)]
        while True:
            c, i, j = heapq.heappop(Q)
            if (i, j) == (n - 1, m - 1):
                return c
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    nc = c + grid[x][y]
                    if nc < cost[x][y]:
                        heapq.heappush(Q, (nc, x, y))
                        cost[x][y] = nc


true, false, null = True, False, None
cases = [
    ([[0, 1, 1], [1, 1, 0], [1, 1, 0]], 2),
    ([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumObstacles, cases)

if __name__ == '__main__':
    pass
