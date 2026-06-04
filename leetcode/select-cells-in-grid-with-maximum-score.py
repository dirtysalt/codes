#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        import functools
        @functools.cache
        def dfs(st, M):
            if st == (1 << n) - 1: return 0
            ans = 0
            for i in range(n):
                if st & (1 << i) == 0:
                    for j in range(m):
                        if grid[i][j] > M:
                            r = dfs(st | (1 << i), grid[i][j])
                            ans = max(r + grid[i][j], ans)
            return ans

        ans = dfs(0, 0)
        return ans


if __name__ == '__main__':
    pass
