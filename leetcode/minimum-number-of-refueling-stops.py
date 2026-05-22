#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0] * (n + 1)
        dp[0] = startFuel

        for i in range(n):
            for c in reversed(range(i + 1)):
                f = dp[c]
                if f >= stations[i][0]:
                    dp[c + 1] = max(dp[c + 1], f + stations[i][1])

        ans = -1
        for c in range(n + 1):
            f = dp[c]
            if f >= target:
                ans = c
                break
        return ans


cases = [
    (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
    (1, 1, [], 0),
    (100, 1, [(10, 100)], -1),
    (100, 25, [[25, 25], [50, 25], [75, 25]], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minRefuelStops, cases)
