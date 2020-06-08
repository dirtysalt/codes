#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = {}
        inf = 1 << 30

        def fun(i, j, t):
            if i == -1:
                return 0 if t == 0 else inf
            if t == 0:
                return inf
            if houses[i] != 0 and houses[i] != j:
                return inf

            key = (i, j, t)
            if key in dp:
                return dp[key]

            ans = inf
            c = 0
            if houses[i] == 0:
                c = cost[i][j - 1]
            for j2 in range(1, n + 1):
                t2 = t if j2 == j else t - 1
                res = c + fun(i - 1, j2, t2)
                ans = min(res, ans)
            dp[key] = ans
            return ans

        ans = inf
        for j in range(1, n + 1):
            res = fun(m - 1, j, target)
            ans = min(res, ans)
        return -1 if ans == inf else ans


cases = [
    ([0, 0], [[1, 10], [10, 1]], 2, 2, 1, 11),
    ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9),
    ([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1),
    ([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11),
    ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5, 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCost, cases)
