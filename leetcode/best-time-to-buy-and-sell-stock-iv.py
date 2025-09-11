#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        k = min(k, n // 2)
        inf = 1 << 20
        sell = [-inf] * (k + 1)
        buy = [-inf] * (k + 1)
        sell[0] = 0
        for i in range(n):
            for kk in reversed(range(k + 1)):
                sell[kk] = max(sell[kk], buy[kk] + prices[i])
                if kk > 0:
                    buy[kk] = max(buy[kk], sell[kk - 1] - prices[i])
        ans = max(sell)
        return ans


cases = [
    (2, [2, 4, 1], 2,),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (2, [1, 2, 4], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProfit, cases)
