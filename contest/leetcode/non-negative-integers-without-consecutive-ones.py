#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findIntegers(self, num: int) -> int:
        dp = {}

        def f(n):
            if n <= 3:
                if n == 3:
                    return 3
                return n + 1

            if n in dp:
                return dp[n]

            x1 = n // 4
            x2 = (n - 1) // 4
            x3 = (n - 2) // 8
            ans = f(x1) + f(x2) + f(x3)
            dp[n] = ans
            return ans

        ans = f(num)
        return ans



cases = [
    (5, 5),
    (10 ** 9, 2178309)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findIntegers, cases)
