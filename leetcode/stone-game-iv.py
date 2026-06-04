#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            win = 0
            for j in range(1, n + 1):
                j2 = j * j
                if j2 > i: break
                if dp[i - j2] == 0:
                    win = 1
                    break
            dp[i] = win
        return bool(dp[n])


cases = [
    (1, True),
    (2, False),
    (7, False),
    (17, False),
    (10 ** 5, True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().winnerSquareGame, cases)
