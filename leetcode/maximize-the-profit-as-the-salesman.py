#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        dp = [0] * (n + 1)
        idx = -1

        for s, e, g in offers:
            while idx <= (s - 1):
                dp[idx] = max(dp[idx], dp[idx - 1])
                idx += 1
            dp[e] = max(dp[s - 1] + g, dp[e])

        return max(dp)


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [[0, 0, 1], [0, 2, 2], [1, 3, 2]], 3),
    (5
     , [[0, 0, 1], [0, 2, 10], [1, 3, 2]], 10),
    (10,
     [[0, 6, 5], [2, 9, 4], [0, 9, 2], [3, 9, 3], [1, 6, 10], [0, 1, 3], [3, 8, 9], [4, 8, 3], [2, 6, 5], [0, 4, 6]],
     12),
]

aatest_helper.run_test_cases(Solution().maximizeTheProfit, cases)

if __name__ == '__main__':
    pass
