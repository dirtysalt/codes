#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp = [[0] * n, [0] * n]
        # dp[0][i] 截止到ith位置，处于sell状态(closed)
        # dp[1][i] 截止到ith位置，处于buy状态(open)

        dp[0][0] = 0
        dp[1][0] = -prices[0]

        # dp[0][i] = dp[1][i-1] + prices[i], dp[0][i-1]
        # dp[1][i] = dp[0][i-2] - prices[i], dp[1][i-1]
        for i in range(1, n):
            dp[0][i] = max(dp[1][i - 1] + prices[i], dp[0][i - 1])
            dp[1][i] = max((dp[0][i - 2] if i >= 2 else 0) - prices[i], dp[1][i - 1])

        ans = dp[0][n - 1]
        return ans


cases = [
    ([1, 2, 3, 0, 2], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProfit, cases)
