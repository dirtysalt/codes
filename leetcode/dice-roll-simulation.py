#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        P = 10 ** 9 + 7
        dp = [[0] * 6 for _ in range(n + 1)]

        for i in range(6):
            for j in range(1, rollMax[i] + 1):
                if j <= n:
                    dp[j][i] += 1

        for k in range(1, n + 1):
            for l, i in ((x, y) for x in range(6) for y in range(6) if x != y):
                for j in range(1, min(rollMax[i] + 1, n - k + 1)):
                    dp[k + j][i] = (dp[k + j][i] + dp[k][l]) % P

        ans = sum(dp[n]) % P
        return ans


cases = [
    (2, [1, 1, 2, 2, 2, 3], 34),
    (3, [1, 1, 1, 2, 2, 3], 181),
    (5000, [15, 15, 15, 15, 15, 15], -1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().dieSimulator, cases)
