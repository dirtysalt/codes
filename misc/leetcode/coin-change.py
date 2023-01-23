#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 1 << 30
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(amount):
            for c in coins:
                if (i + c) <= amount:
                    dp[i + c] = min(dp[i + c], dp[i] + 1)

        ans = dp[amount]
        if ans == inf:
            ans = -1
        return ans


cases = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().coinChange, cases)
