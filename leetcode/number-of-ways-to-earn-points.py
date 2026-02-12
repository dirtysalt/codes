#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for c, m in types:
            for t in reversed(range(target + 1)):
                for j in range(1, c + 1):
                    t2 = j * m + t
                    if t2 > target: break
                    dp[t2] = (dp[t2] + dp[t]) % MOD
        return dp[target]


true, false, null = True, False, None
import aatest_helper

cases = [
    (6, [[6, 1], [3, 2], [2, 3]], 7),
    (5, [[50, 1], [50, 2], [50, 5]], 4),
    (18, [[6, 1], [3, 2], [2, 3]], 1),
]

aatest_helper.run_test_cases(Solution().waysToReachTarget, cases)

if __name__ == '__main__':
    pass
