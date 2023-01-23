#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        inf = 1 << 30
        dp = []
        # dp[i][t][j]
        for i in range(m + 1):
            dp.append([[inf] * (1 + n) for _ in range(1 + target)])
        dp[0][0][0] = 0

        for i in range(1, m + 1):
            for t in range(1 + target):
                for j in range(1, n + 1):
                    if houses[i - 1] == 0:
                        c = cost[i - 1][j - 1]
                    elif houses[i - 1] == j:
                        c = 0
                    else:
                        c = inf

                    res = inf
                    for j2 in range(n + 1):
                        t2 = t if j == j2 else t - 1
                        v = dp[i - 1][t2][j2] if t2 >= 0 else inf
                        res = min(res, c + v)
                    dp[i][t][j] = res

        ans = min(dp[m][target][1:n + 1])
        return -1 if ans == inf else ans


cases = [
    ([0, 0], [[1, 10], [10, 1]], 2, 2, 1, 11),
    ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9),
    ([3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1),
    ([0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11),
    ([0, 0, 0, 0, 0], [[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], 5, 2, 5, 5),
    ([3, 0, 3, 4, 0, 5, 4, 0, 0, 5, 0, 0, 0, 2, 5, 1, 0],
     [[14, 1, 16, 14, 19], [5, 18, 3, 19, 20], [6, 2, 4, 20, 15], [13, 7, 10, 1, 11], [19, 18, 9, 15, 11],
      [4, 19, 7, 8, 20], [6, 7, 12, 5, 7], [4, 20, 18, 13, 1], [16, 2, 11, 6, 17], [2, 3, 1, 5, 12], [3, 9, 13, 5, 4],
      [9, 3, 9, 2, 19], [2, 10, 15, 5, 11], [18, 10, 10, 4, 3], [6, 8, 17, 10, 19], [11, 13, 1, 16, 6],
      [15, 12, 16, 5, 11]]
     , 17, 5, 4, -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCost, cases)
