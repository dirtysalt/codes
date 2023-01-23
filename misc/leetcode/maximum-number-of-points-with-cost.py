#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = [[0] * m for _ in range(2)]
        for j in range(m):
            dp[0][j] = points[0][j]

        # dp[i][j] = max(dp[i-1][k] - abs(k-j)) + points[i][j]
        now = 0
        for i in range(1, n):
            left = [0] * m
            right = [0] * m

            mx = -(1 << 30)
            for j in range(m):
                mx = max(dp[now][j], mx - 1)
                left[j] = mx

            mx = -(1 << 30)
            for j in reversed(range(m)):
                mx = max(dp[now][j], mx - 1)
                right[j] = mx

            for j in range(m):
                dp[1 - now][j] = max(left[j], right[j]) + points[i][j]
            now = 1 - now

        return max(dp[now])


true, false, null = True, False, None
cases = [
    ([[1, 2, 3], [1, 5, 1], [3, 1, 1]], 9),
    ([[1, 5], [2, 3], [4, 2]], 11),
    ([[3], [4], [2], [0]], 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxPoints, cases)

if __name__ == '__main__':
    pass
