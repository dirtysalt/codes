#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [-1] * (N + 1)

        def search(n):
            if dp[n] != -1:
                return dp[n]

            ans = 0
            for x in range(1, n):
                if n % x != 0: continue
                if search(n - x) == 0:
                    ans = 1
                    break
            dp[n] = ans
            return ans

        ans = search(N)
        print(dp)
        return ans


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


cases = [
    (2, True),
    (3, False),
    (10, True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().divisorGame, cases)
