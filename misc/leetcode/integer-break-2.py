#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def integerBreak(self, n: int) -> int:

        dp = list(range(n + 1))

        for i in range(1, n + 1):
            res = 0
            for j in range(1, i):
                res = max(res, (i - j) * max(dp[j], j))
            dp[i] = res

        # ans = max(dp)
        ans = dp[-1]
        return ans
