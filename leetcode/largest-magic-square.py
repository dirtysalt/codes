#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        row = [[0] * (m + 1) for _ in range(n)]
        col = [[0] * (n + 1) for _ in range(m)]

        for i in range(n):
            for j in range(m):
                row[i][j + 1] = row[i][j] + grid[i][j]
        for j in range(m):
            for i in range(n):
                col[j][i + 1] = col[j][i] + grid[i][j]

        maxK = 0
        for i in range(n):
            for j in range(m):
                K = min(n - i, m - j)
                for k in reversed(range(1, K + 1)):
                    base = row[i][j + k] - row[i][j]
                    ok = True
                    for z in range(k):
                        delta = row[i + z][j + k] - row[i + z][j]
                        if delta != base:
                            ok = False
                            break
                        delta = col[j + z][i + k] - col[j + z][i]
                        if delta != base:
                            ok = False
                            break

                    if not ok:
                        continue

                    # diagonal
                    t1 = t2 = 0
                    for z in range(k):
                        t1 += grid[i + z][j + z]
                        t2 += grid[i + z][j + k - 1 - z]
                    if t1 != base or t2 != base:
                        continue

                    maxK = max(maxK, k)
                    break
        return maxK


true, false, null = True, False, None
cases = [
    ([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]], 3),
    ([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]], 2),
    ([[1, 9, 3, 5, 5, 8, 1, 6, 9], [4, 1, 1, 6, 8, 3, 5, 7, 6], [9, 8, 4, 7, 2, 4, 9, 2, 7],
      [1, 9, 8, 10, 5, 10, 1, 6, 3]], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestMagicSquare, cases)

if __name__ == '__main__':
    pass
