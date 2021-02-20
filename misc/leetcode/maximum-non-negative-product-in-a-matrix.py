#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        M0 = [[-1] * m for _ in range(n)]
        M1 = [[-1] * m for _ in range(n)]
        M1[0][0] = M0[0][0] = grid[0][0]
        inf = 1 << 63
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0: continue
                a, b = -inf, inf
                x = grid[i][j]
                if (i - 1) >= 0:
                    m0, m1 = M0[i - 1][j], M1[i - 1][j]
                    a = max(a, m0 * x, m1 * x)
                    b = min(b, m0 * x, m1 * x)
                if (j - 1) >= 0:
                    m0, m1 = M0[i][j - 1], M1[i][j - 1]
                    a = max(a, m0 * x, m1 * x)
                    b = min(b, m0 * x, m1 * x)
                M0[i][j] = a
                M1[i][j] = b
                # print(i, j, a, b)
        if M0[i][j] < 0: return -1
        MOD = 10 ** 9 + 7
        ans = M0[i][j] % MOD
        return ans


cases = [
    ([[-1, -2, -3],
      [-2, -3, -3],
      [-3, -3, -2]], -1),
    ([[1, -2, 1],
      [1, -2, 1],
      [3, -4, 1]], 8),
    ([[1, 3],
      [0, -4]], 0),
    ([[1, 4, 4, 0],
      [-2, 0, 0, 1],
      [1, -1, 1, 1]], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProductPath, cases)
