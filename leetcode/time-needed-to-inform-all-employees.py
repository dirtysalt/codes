#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dp = [-1] * n

        def f(i):
            if i == headID:
                return 0
            if dp[i] != -1:
                return dp[i]
            j = manager[i]
            ans = informTime[j] + f(j)
            dp[i] = ans
            return ans

        ans = 0
        for i in range(n):
            ans = max(ans, f(i))
        return ans


cases = [
    (7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1], 21)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numOfMinutes, cases)
