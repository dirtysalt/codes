#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        dp = {}

        def fun(g, p, i):
            if i == -1:
                if p >= P:
                    return 1
                return 0

            g = min(g, G)
            p = min(p, P)

            key = (g, p, i)
            if key in dp:
                return dp[key]

            ans = 0
            if (group[i] + g) <= G:
                t = fun(group[i] + g, p + profit[i], i - 1)
                ans += t
            t = fun(g, p, i - 1)
            ans += t
            dp[key] = ans
            return ans

        MOD = 10 ** 9 + 7
        n = len(profit)
        ans = fun(0, 0, n - 1)
        # print(dp)
        return ans % MOD
