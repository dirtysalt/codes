#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        def cost(x, p):
            return max(x - p, 1)

        n, m = len(dungeon), len(dungeon[0])
        inf = (1 << 30)
        dp = [[inf] * m for _ in range(n)]
        dp[n - 1][m - 1] = cost(1, dungeon[n - 1][m - 1])

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                x = dp[i][j]
                if i >= 1:
                    dp[i - 1][j] = min(dp[i - 1][j], cost(x, dungeon[i - 1][j]))
                if j >= 1:
                    dp[i][j - 1] = min(dp[i][j - 1], cost(x, dungeon[i][j - 1]))

        # print(dp)
        return dp[0][0]
