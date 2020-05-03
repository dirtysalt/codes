#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode import aatest_helper


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n表示总金额，m表示[0..m]这些coins可以选择
        # dp[n][m] = dp[n][m-1] + dp[n-coins[m]][m]
        if not coins:
            if amount == 0:
                return 1
            return 0

        n, m = amount + 1, len(coins)

        dp = []
        for i in range(n):
            dp.append([0] * m)
        for i in range(m):
            dp[0][i] = 1

        for v in range(1, n):
            for c in range(m):
                res = 0
                if (v - coins[c]) >= 0:
                    res += dp[v - coins[c]][c]
                if c >= 0:
                    res += dp[v][c - 1]
                dp[v][c] = res

        return dp[n - 1][m - 1]


sol = Solution()
cases = [
    (5, [1, 2, 5, ], 4),
    (3, [2], 0),
    (10, [10], 1)
]

aatest_helper.run_test_cases(sol.change, cases)
