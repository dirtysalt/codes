#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[0] * 10 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                dist[j][grid[i][j]] += 1

        inf = 1 << 30

        @functools.cache
        def dfs(i, x):
            if i == m: return 0
            ans = inf
            for j in range(10):
                if j == x: continue
                c = n - dist[i][j]
                r = c + dfs(i + 1, j)
                ans = min(ans, r)
            return ans

        ans = dfs(0, -1)
        return ans


if __name__ == '__main__':
    pass
