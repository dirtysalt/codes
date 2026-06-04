#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         # dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... dp[n-1][max(k-n+1, 0)]
#
#         dp = [[0] * (k + 1) for _ in range(n + 1)]
#         dp[1][0] = 1
#
#         for i in range(1, n):
#             for j in range(0, k + 1):
#                 for off in range(0, i + 1):
#                     if (off + j) > k:
#                         break
#                     dp[i + 1][off + j] += dp[i][j]
#
#         # print(dp)
#         return dp[n][k]


#
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # dp[n][k] = dp[n-1][k] + dp[n-1][k-1] + ... dp[n-1][max(k-n+1, 0)]
        # 这个状态方程需要计算优化

        MOD = 10 ** 9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = 1

        for i in range(2, n + 1):
            acc = 0
            for j in range(0, k + 1):
                # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] + ... dp[i - 1][j - i + 1] + (dp[i-1][j-i])
                acc += dp[i - 1][j]
                if j >= i:
                    acc -= dp[i - 1][j - i]
                acc = acc % MOD
                dp[i][j] = (acc + dp[i][j]) % MOD

        # print(dp)
        return dp[n][k]


cases = [
    (3, 0, 1),
    (3, 1, 2),
    (1000, 1000, 663677020),
    (2, 2, 0)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().kInversePairs, cases)
