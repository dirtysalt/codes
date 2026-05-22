#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        for K in range(min(n, m) // 2):
            # start from (k, k)
            R = n - K * 2
            C = m - K * 2
            idx = []
            r, c = K, K
            for i in range(C - 1):
                idx.append((r, c))
                c += 1

            for i in range(R - 1):
                idx.append((r, c))
                r += 1

            for i in range(C - 1):
                idx.append((r, c))
                c -= 1

            for i in range(R - 1):
                idx.append((r, c))
                r -= 1

            # print(idx)
            values = []
            for i in range(len(idx)):
                r, c = idx[(i + k) % len(idx)]
                values.append(grid[r][c])
            for i in range(len(idx)):
                v = values[i]
                r, c = idx[i]
                grid[r][c] = v

        return grid


true, false, null = True, False, None
cases = [
    ([[40, 10], [30, 20]], 1, [[10, 20], [40, 30]]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2,
     [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().rotateGrid, cases)

if __name__ == '__main__':
    pass
