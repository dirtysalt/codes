#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def oneside(xs):
            n = len(xs)
            dp = [[1] * n, [0] * n, [0] * n]

            res = 0
            for i in range(1, n):
                for j in range(i):
                    if xs[i] > xs[j]:
                        dp[1][i] += dp[0][j]
                        dp[2][i] += dp[1][j]
                        res += dp[1][j]

            # print(dp, res)
            return res

        ans = oneside(rating)
        ans += oneside(rating[::-1])
        return ans


cases = [
    ([2, 5, 3, 4, 1], 3),
    ([2, 1, 3], 0),
    ([1, 2, 3, 4], 4)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().numTeams, cases)
