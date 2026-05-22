#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def precompute():
            dp = [[0] * (k) for _ in range(n + 1)]
            dp[0][0] = 1
            for i in range(n):
                for j in range(0, k):
                    j2 = nums[i] + j
                    if j2 < k:
                        dp[i + 1][j2] += dp[i][j]
                    dp[i + 1][j] += dp[i][j]
            return dp

        def pow(a, b, MOD):
            ans = 1
            while b:
                if b & 0x1:
                    ans = ans * a
                    ans = ans % MOD
                a = (a * a) % MOD
                b = b >> 1
            return ans

        # (G1, G2) = (2**n) % MOD
        # G1<k = dp[n][j] j in [0, k)
        # G2<k = dp[n][j] j in [0, k)
        # G1<k & G2<k  = dp[n][j] j in [0,k) and (SUM-j) in [0,k)
        # (G1,G2) - (G1<k) - (G2<k) + (G1<k & G2<k) = (G1>=k & G2>=k)
        dp = precompute()
        SUM = sum(nums)
        MOD = 10 ** 9 + 7
        ans = pow(2, n, MOD)
        for j in range(0, k):
            ans -= 2 * dp[n][j]
        for j in range(0, k):
            if (SUM - j) < k:
                ans += dp[n][j]
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4], 4, 6),
    ([3, 3, 3, ], 4, 0),
    ([6, 6, ], 2, 2),
]

aatest_helper.run_test_cases(Solution().countPartitions, cases)

if __name__ == '__main__':
    pass
