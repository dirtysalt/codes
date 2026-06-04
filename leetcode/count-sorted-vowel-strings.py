#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1

        for i in range(1, n):
            acc = 0
            for j in range(5):
                acc += dp[i - 1][j]
                dp[i][j] = acc

        ans = sum(dp[-1])
        return ans


cases = [
    (1, 5),
    (2, 15),
    (33, 66045)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countVowelStrings, cases)
