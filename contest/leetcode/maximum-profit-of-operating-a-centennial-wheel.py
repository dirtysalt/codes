#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        w = 0
        ans = -1
        count = 0
        max_profit = 0

        for c in customers:
            w += c
            x = min(w, 4)
            w -= x
            profit += x * boardingCost - runningCost
            count += 1
            if profit > max_profit:
                max_profit = profit
                ans = count

        while w > 0:
            x = min(w, 4)
            w -= x
            profit += x * boardingCost - runningCost
            count += 1
            if profit > max_profit:
                max_profit = profit
                ans = count

        return ans


cases = [
    ([8, 3], 5, 6, 3),
    ([10, 9, 6], 6, 4, 7),
    ([3, 4, 0, 5, 1], 1, 92, -1),
    ([10, 10, 6, 4, 7], 3, 8, 9),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperationsMaxProfit, cases)
