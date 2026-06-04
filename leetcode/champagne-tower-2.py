#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for i in range(query_row):
            dp2 = [0] * (len(dp) + 1)
            for j in range(len(dp2)):
                res = 0
                if j >= 1 and dp[j - 1] >= 1:
                    res += (dp[j - 1] - 1) * 0.5
                if j < len(dp) and dp[j] >= 1:
                    res += (dp[j] - 1) * 0.5
                dp2[j] = res
            dp = dp2
        ans = min(1, dp[query_glass])
        return ans


cases = [
    (4, 2, 1, 0.5),
    (2, 1, 1, 0.5),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().champagneTower, cases)
