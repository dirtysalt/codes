#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                a, b = i, j
                d = 0
                while a < b:
                    d += houses[b] - houses[a]
                    a += 1
                    b -= 1
                dist[i][j] = d

        inf = 1 << 30
        dp = {}

        def test(i, k):
            if i == n:
                return 0 if k == 0 else inf
            if k == 0:
                return inf

            key = (i, k)
            if key in dp:
                return dp[key]

            ans = inf
            for j in range(i, n):
                res = test(j + 1, k - 1)
                res = res + dist[i][j]
                ans = min(ans, res)
            dp[key] = ans
            return ans

        ans = test(0, k)
        return ans


cases = [
    ([1, 4, 8, 10, 20], 3, 5),
    ([2, 3, 5, 12, 18], 2, 9),
    ([7, 4, 6, 1], 1, 8),
    ([3, 6, 14, 10], 4, 0),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().minDistance, cases)
