#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        start = grid[0][0]
        dp[0][0][start % k] = 1

        MOD = 10 ** 9 + 7
        for i in range(n):
            for j in range(m):
                if i < n - 1:
                    i2, j2 = i + 1, j
                    v = grid[i2][j2]
                    for kk in range(k):
                        dp[i2][j2][(kk + v) % k] += dp[i][j][kk]
                if j < m - 1:
                    i2, j2 = i, j + 1
                    v = grid[i2][j2]
                    for kk in range(k):
                        dp[i2][j2][(kk + v) % k] += dp[i][j][kk]

        ans = dp[n - 1][m - 1][0]
        ans = ans % MOD
        return ans


true, false, null = True, False, None
cases = [
    ([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3, 2),
    ([[0, 0]], 5, 1),
    ([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1, 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfPaths, cases)

if __name__ == '__main__':
    pass
