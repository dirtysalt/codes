#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        dp = [[0] * (k + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(1, N + 1):
            for j in range(k + 1):
                dp[i][j] = ((dp[i - 1][j - 1] if j >= 1 else 0) + dp[i - 1][j]) % MOD

        def solve(nums):
            ans = 0
            for i in range(N):
                cnt = 0
                for j in range(min(i + 1, k)):
                    cnt += dp[i][j]
                ans += (cnt * nums[i]) % MOD
                ans %= MOD
            return ans

        A = solve(sorted(nums))
        B = solve(sorted(nums, reverse=True))
        return (A + B) % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 2, 24),
    ([5, 0, 6], 1, 22),
    ([1, 1, 1], 2, 12),
]

aatest_helper.run_test_cases(Solution().minMaxSums, cases)

if __name__ == '__main__':
    pass
