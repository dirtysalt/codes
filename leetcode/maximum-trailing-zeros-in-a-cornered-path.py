#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row = [[(0, 0)] * (m + 1) for _ in range(n)]
        col = [[(0, 0)] * (n + 1) for _ in range(m)]

        def decompose(x):
            x2 = x
            a, b = 0, 0
            while x % 2 == 0:
                a += 1
                x = x // 2
            while x % 5 == 0:
                b += 1
                x = x // 5
            # print(x2, a, b)
            return a, b

        for i in range(n):
            for j in range(m):
                x = grid[i][j]
                a, b = decompose(x)
                row[i][j + 1] = (row[i][j][0] + a, row[i][j][1] + b)

        for j in range(m):
            for i in range(n):
                x = grid[i][j]
                a, b = decompose(x)
                col[j][i + 1] = (col[j][i][0] + a, col[j][i][1] + b)

        ans = 0
        for i in range(n):
            for j in range(m):
                r0, r1 = decompose(grid[i][j])

                # i, j as turing point.
                R, C = [], []

                # X axis
                a, b = row[i][j + 1]
                R.append((a, b))

                a, b = row[i][m]
                c, d = row[i][j]
                a, b = a - c, b - d
                R.append((a, b))

                # Y axis
                a, b = col[j][i + 1]
                C.append((a, b))

                a, b = col[j][n]
                c, d = col[j][i]
                a, b = a - c, b - d
                C.append((a, b))

                for a, b in R:
                    for c, d in C:
                        res = min(a + c - r0, b + d - r1)
                        ans = max(ans, res)

        return ans


true, false, null = True, False, None
cases = [
    ([[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]], 3),
    ([[4, 3, 2], [7, 6, 1], [8, 8, 8]], 0),
    ([[1, 5, 2, 4, 25]], 3),
    ([[242, 921, 651, 509, 130, 857], [486, 959, 4, 159, 150, 655], [825, 644, 838, 771, 101, 199],
      [781, 770, 193, 492, 930, 670], [395, 474, 960, 839, 616, 652], [895, 156, 833, 124, 863, 907],
      [603, 921, 383, 279, 654, 933]], 6),
    ([[534, 575, 625, 84, 20, 999, 35], [208, 318, 96, 380, 819, 102, 669]], 8),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxTrailingZeros, cases)

if __name__ == '__main__':
    pass
