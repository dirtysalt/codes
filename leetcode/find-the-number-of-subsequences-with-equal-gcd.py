#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        M = max(nums) + 1
        dp = [[0] * M for _ in range(M)]
        dp[0][0] = 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        MOD = 10 ** 9 + 7
        for i in range(len(nums)):
            ndp = [[0] * M for _ in range(M)]
            for g1 in range(M):
                for g2 in range(M):
                    if dp[g1][g2] == 0: continue
                    ndp[g1][g2] += dp[g1][g2]
                    # nums[i] -> g1 or g2
                    g = gcd(g1, nums[i])
                    ndp[g][g2] += dp[g1][g2]
                    g = gcd(g2, nums[i])
                    ndp[g1][g] += dp[g1][g2]

            for g1 in range(M):
                for g2 in range(M):
                    dp[g1][g2] %= MOD
            dp = ndp

        ans = 0
        for g in range(1, M):
            ans += dp[g][g]
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4], 10),
    ([10, 20, 30], 2),
    ([1, 1, 1, 1], 50),
]

aatest_helper.run_test_cases(Solution().subsequencePairCount, cases)

if __name__ == '__main__':
    pass
