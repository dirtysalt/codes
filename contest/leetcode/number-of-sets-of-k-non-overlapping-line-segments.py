#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def fun(x, k):
            if k == 0:
                return 1

            key = (x, k)
            if key in dp: return dp[key]
            ans = 0
            for y in range(x + 1, n):
                # [x, y] is available
                # there are y - x solutions.
                sz = y - x
                ans += sz * fun(y, k - 1)
            ans = ans % MOD
            dp[key] = ans
            return ans

        ans = fun(0, k)
        return ans


cases = [
    (4, 2, 5),
    (3, 1, 3,),
    (30, 7, 796297179),
    (5, 3, 7),
    (3, 2, 1),
    # (1000, 999, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfSets, cases)
