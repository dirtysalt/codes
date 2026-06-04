#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def fun(x, k):
            if k == 0:
                return 1

            key = (x, k)
            if key in dp: return dp[key]
            ans = 0
            for y in range(x + 1, n):
                # [x, y] is available
                # there are y - x solutions.
                sz = y - x
                ans += sz * fun(y, k - 1)
            ans = ans % MOD
            dp[key] = ans
            return ans

        ans = fun(0, k)
        return ans


class Solution2:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(k + 1)]

        # dp[k][x] 以 x结束，可以分为k段的组合数
        for i in range(n):
            dp[1][i] = i

        for kk in range(2, k + 1):
            acc = 0
            for i in range(n - 1):
                acc += dp[kk - 1][i]
                dp[kk][i + 1] = dp[kk][i] + acc

        ans = 0
        for i in range(n):
            ans += dp[k][i]
        return ans % MOD


class Solution3:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(2)]

        # dp[k][x] 以x结束，可以分为k段的组合数
        for i in range(n):
            dp[0][i] = i

        now = 0
        for kk in range(2, k + 1):
            to = 1 - now
            acc = 0
            for i in range(n - 1):
                acc += dp[now][i]
                dp[to][i + 1] = dp[to][i] + acc
            now = to

        ans = 0
        for i in range(n):
            ans += dp[now][i]
        return ans % MOD


cases = [
    (4, 2, 5),
    (3, 1, 3,),
    (30, 7, 796297179),
    (5, 3, 7),
    (3, 2, 1),
    (1000, 999, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution3().numberOfSets, cases)
