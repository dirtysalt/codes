#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        values = []
        up, down = {}, {}
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                up[(i, j, 0)] = v
                down[(i, j, 0)] = v

                k = 1
                while True:
                    l, r = j - k, j + k
                    if (i + k) >= n or l < 0 or r >= m: break
                    v += grid[i + k][l] + grid[i + k][r]
                    up[(i, j, k)] = v
                    k += 1

                k = 1
                v = grid[i][j]
                while True:
                    l, r = j - k, j + k
                    if (i - k) < 0 or l < 0 or r >= m: break
                    v += grid[i - k][l] + grid[i - k][r]
                    down[(i, j, k)] = v
                    k += 1

        for i in range(n):
            for j in range(m):
                values.append(grid[i][j])
                k = 1
                while True:
                    i2 = i + 2 * k
                    l, r = j - k, j + k
                    if i2 >= n or l < 0 or r >= m: break
                    a = up[(i, j, k)]
                    b = down[(i2, j, k - 1)]
                    values.append(a + b)
                    k += 1

        values = list(set(values))
        values.sort(reverse=True)
        return values[:3]

true, false, null = True, False, None
cases = []

import aatest_helper
aatest_helper.run_test_cases(Solution().getBiggestThree, cases)


if __name__ == '__main__':
    pass
