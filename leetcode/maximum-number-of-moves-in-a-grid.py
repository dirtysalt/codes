#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [0] * n

        ans = 0
        for j in range(m - 1):
            dp2 = [-1] * n
            for i in range(n):
                if dp[i] == -1: continue
                for d in (-1, 0, 1):
                    if 0 <= (i + d) < n and grid[i + d][j + 1] > grid[i][j]:
                        dp2[i + d] = max(dp2[i + d], dp[i] + 1)
            dp = dp2
            ans = max(ans, max(dp))
        return ans


if __name__ == '__main__':
    pass
