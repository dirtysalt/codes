#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(d):
            for t in reversed(range(target + 1)):
                ans = 0
                for j in range(1, f + 1):
                    ans += dp[t - j] if t >= j else 0
                dp[t] = ans % MOD
        ans = dp[target]
        return ans


cases = [
    (1, 6, 3, 1),
    (2, 6, 7, 6),
    (2, 5, 10, 1),
    (1, 2, 3, 0),
    (30, 30, 500, 222616187),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numRollsToTarget, cases)
