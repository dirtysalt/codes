#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        inf = (1 << 30)
        dp = [[inf] * m, [inf] * m]
        dp[0][0] = 0
        now = 0

        for i in range(n):
            for j in range(m):
                dp[1 - now][j] = grid[i][j] + min(dp[now][j], dp[1 - now][j - 1] if j > 0 else inf)
            now = 1 - now
        ans = dp[now][-1]
        return ans
