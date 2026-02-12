#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n, m = len(coins), len(coins[0])
        inf = 1 << 30
        dp = [[[-inf] * 3 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = dp[0][0][2] = max(coins[0][0], 0)

        for i in range(n):
            for j in range(m):
                for dx, dy in ((1, 0), (0, 1)):
                    if (i + dx) >= n or (j + dy) >= m: continue
                    x, y = i + dx, j + dy
                    for d in range(3):
                        dp[x][y][d] = max(dp[x][y][d], dp[i][j][d] + coins[x][y])
                        if (d + 1) < 3:
                            dp[x][y][d + 1] = max(dp[x][y][d + 1], dp[i][j][d] + max(coins[x][y], 0))

        return max(dp[-1][-1])


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 1, -1], [1, -2, 3], [2, -3, 4]], 8),
    ([[10, 10, 10], [10, 10, 10]], 40),
]

aatest_helper.run_test_cases(Solution().maximumAmount, cases)

if __name__ == '__main__':
    pass
