#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = {}
        inf = 1 << 30

        def query(i, j, cuts):
            if len(cuts) == 0:
                return 0

            key = (i, j)
            if key in dp:
                return dp[key]

            ans = inf
            for k in range(len(cuts)):
                kk = cuts[k]
                a = query(i, kk, cuts[:k])
                b = query(kk, j, cuts[k + 1:])
                cost = a + b + (j - i)
                ans = min(ans, cost)

            dp[key] = ans
            return ans

        cuts.sort()
        ans = query(0, n, cuts)
        return ans


cases = [
    (7, [1, 3, 4, 5], 16),
    (9, [5, 6, 1, 4, 2], 22),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCost, cases)
