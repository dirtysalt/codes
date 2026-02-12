#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        acc = stoneValue.copy()
        acc.insert(0, 0)
        for i in range(n):
            acc[i + 1] += acc[i]

        dp = {}

        def fun(s, e):
            if s == e: return 0
            key = (s, e)
            if key in dp: return dp[key]

            ans = 0
            for k in range(s, e + 1):
                p0 = acc[k + 1] - acc[s]
                p1 = acc[e + 1] - acc[k + 1]
                if p0 < p1:
                    t = p0 + fun(s, k)
                elif p0 > p1:
                    t = p1 + fun(k + 1, e)
                else:
                    t = p0 + max(fun(s, k), fun(k + 1, e))
                ans = max(ans, t)
            dp[key] = ans
            return ans

        ans = fun(0, n - 1)
        return ans


cases = [
    ([6, 2, 3, 4, 5, 5], 18),
    ([7, 7, 7, 7, 7, 7, 7], 28),
    ([4], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().stoneGameV, cases)
