#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        from math import inf
        ans = -inf
        dp = [-inf] * m
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                M = dp[j]
                if (j + 1) < m: M = max(M, dp[j + 1])
                ans = max(M - grid[i][j], ans)
                dp[j] = max(M, grid[i][j])
        return ans


if __name__ == '__main__':
    pass
