#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]

        orders = []
        for i in range(n):
            for j in range(m):
                orders.append((grid[i][j], i, j))
        orders.sort()

        MOD = 10 ** 9 + 7
        ans = 0
        for x, i, j in orders:
            dp[i][j] += 1
            ans += dp[i][j]
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2, j2 = i + dx, j + dy
                if 0 <= i2 < n and 0 <= j2 < m and grid[i2][j2] > x:
                    dp[i2][j2] += dp[i][j]

        return ans % MOD


true, false, null = True, False, None
cases = [
    ([[1, 1], [3, 4]], 8),
    ([[1], [2]], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPaths, cases)

if __name__ == '__main__':
    pass
