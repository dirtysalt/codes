#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countHousePlacements(self, n: int) -> int:

        dp = [[0] * 4 for _ in range(n + 1)]
        dp[0] = [1, 0, 0, 0]

        MOD = 10 ** 9 + 7

        for k in range(n):
            for st in range(4):
                i, j = st // 2, st % 2
                for st2 in range(4):
                    a, b = st2 // 2, st2 % 2
                    if (i == a == 1) or (j == b == 1): continue
                    dp[k + 1][st] += dp[k][st2]
                dp[k + 1][st] %= MOD

        return sum(dp[-1]) % MOD


true, false, null = True, False, None
cases = [
    (1, 4),
    (2, 9),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countHousePlacements, cases)

if __name__ == '__main__':
    pass
