#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minDays(self, n: int) -> int:
        dp = {}

        def fun(k):
            if k in (0, 1): return k
            if k in dp: return dp[k]
            a = fun(k // 2) + k % 2 + 1
            b = fun(k // 3) + k % 3 + 1
            ans = min(a, b)
            dp[k] = ans
            return ans

        ans = fun(n)
        return ans


cases = [
    (10, 4),
    (6, 3,),
    (1, 1,),
    (56, 6),
    (429, 12),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDays, cases)
