#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        dp = {}

        def f(x):
            if x == 1:
                return 0
            if x in dp:
                return dp[x]
            if x % 2 == 0:
                ans = f(x // 2) + 1
            else:
                ans = f(3 * x + 1) + 1
            dp[x] = ans
            return ans

        tmp = [(f(x), x) for x in range(lo, hi + 1)]
        tmp.sort()
        # print(tmp)
        return tmp[k - 1][1]


cases = [
    (12, 15, 2, 13),
    (1, 1000, 2, 2),
    (7, 11, 4, 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getKth, cases)
