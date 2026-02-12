#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        inf = 1 << 30
        dp = [[inf] * m for _ in range(n)]
        dp[0][0] = 0

        import heapq
        hp = []
        heapq.heappush(hp, (0, 0, 0))

        while hp:
            (c, i, j) = heapq.heappop(hp)
            if c != dp[i][j]:
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    c2 = abs(heights[x][y] - heights[i][j])
                    c2 = max(c, c2)
                    if c2 < dp[x][y]:
                        dp[x][y] = c2
                        heapq.heappush(hp, (c2, x, y))
        # print(dp)
        ans = dp[n - 1][m - 1]
        return ans


cases = [
    ([[1, 2, 2], [3, 8, 2], [5, 3, 5]], 2),
    ([[1, 2, 3], [3, 8, 4], [5, 3, 5]], 1),
    ([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumEffortPath, cases)
