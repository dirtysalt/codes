#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        n = len(tires)
        cost = [changeTime] * n
        factor = [1] * n
        T = 20
        best = [0] * T
        for t in range(T):
            for i in range(n):
                cost[i] += tires[i][0] * factor[i]
                factor[i] *= tires[i][1]
            best[t] = min(cost)

        dp = [1 << 30] * (1 + numLaps)
        dp[0] = 0
        for i in range(numLaps):
            for t in range(T):
                j = i + t + 1
                if j <= numLaps:
                    dp[j] = min(dp[j], dp[i] + best[t])
        return dp[numLaps] - changeTime

true, false, null = True, False, None
cases = [
    ([[2, 3], [3, 4]], 5, 4, 21),
    ([[1, 10], [2, 2], [3, 4]], 6, 5, 25),
    ([[99, 7]], 85, 95, 17395),
    (
        [[96, 3], [68, 2], [53, 4], [60, 8], [29, 8], [96, 8], [31, 10], [5, 4], [49, 6], [54, 7], [90, 7], [7, 7],
         [97, 2],
         [50, 9], [34, 2], [89, 7], [51, 7], [73, 3], [42, 4], [24, 7], [99, 3], [34, 10], [33, 9], [45, 7], [32, 2],
         [59, 2], [76, 3], [10, 6], [78, 7], [19, 4], [65, 2], [30, 9], [10, 5], [84, 5], [62, 4], [87, 2], [59, 8],
         [29, 5], [40, 4], [76, 6]], 15, 71, 1405),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumFinishTime, cases)

if __name__ == '__main__':
    pass
