#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1: return 6
        sel = [
            [2, 3, 4, 5, 6],
            [1, 3, 5],
            [1, 2, 4, 5],
            [1, 3, 5],
            [1, 2, 3, 4, 6],
            [1, 5],
        ]
        MOD = 10 ** 9 + 7
        dp = [[0] * 36 for _ in range(n)]
        for i in range(6):
            for j in sel[i]:
                x = (j - 1) * 6 + i
                assert (i != (j - 1))
                dp[1][x] = 1

        for k in range(1, n):
            for st in range(36):
                a, b = st // 6, st % 6
                if dp[k - 1][st] == 0: continue
                for i in range(6):
                    if i == b or (a + 1) not in sel[i]: continue
                    dp[k][i * 6 + a] += dp[k - 1][st]
            for st in range(36):
                dp[k][st] %= MOD

        return sum(dp[-1]) % MOD


true, false, null = True, False, None
cases = [
    (4, 184),
    (2, 22)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().distinctSequences, cases)

if __name__ == '__main__':
    pass
