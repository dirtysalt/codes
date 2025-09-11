#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])

        import functools

        @functools.cache
        def dfs(i, j, x):
            x = x ^ grid[i][j]
            if (i, j) == (n - 1, m - 1):
                return x == k

            res = 0
            if (i + 1) < n:
                res += dfs(i + 1, j, x)
            if (j + 1) < m:
                res += dfs(i, j + 1, x)
            return res

        mod = 10 ** 9 + 7
        ans = dfs(0, 0, 0)
        dfs.cache_clear()
        return ans % mod


if __name__ == '__main__':
    pass
