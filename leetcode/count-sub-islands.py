#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])

        vis = set()

        def dfs(i, j, path):
            vis.add((i, j))
            path.append((i, j))
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    if grid2[x][y] == 1:
                        if (x, y) not in vis:
                            dfs(x, y, path)

        def check(i, j):
            path = []
            dfs(i, j, path)
            for (x, y) in path:
                if grid1[x][y] == 0:
                    return False
            return True

        ans = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in vis and grid2[i][j] == 1 and grid1[i][j] == 1:
                    ok = check(i, j)
                    if ok:
                        ans += 1
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]],
     [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], 3),
    ([[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1]],
     [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]], 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSubIslands, cases)

if __name__ == '__main__':
    pass
