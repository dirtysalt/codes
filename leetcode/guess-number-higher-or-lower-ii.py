#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = {}
        inf = 1 << 30

        def query(i, j):
            if i >= j: return 0
            if (i + 1) == j: return i
            if (i + 2) == j: return i + 1
            key = (i, j)
            if key in dp: return dp[key]

            ans = inf
            for k in range(i + 1, j):
                a = query(i, k - 1)
                if (k + a) > ans: continue
                b = query(k + 1, j)
                if (k + b) > ans: continue
                t = k + max(a, b)
                ans = min(ans, t)
            dp[key] = ans

            return ans

        ans = query(1, n)
        # print(dp)
        return ans


cases = [
    (10, 16),
    (100, 400)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getMoneyAmount, cases)
