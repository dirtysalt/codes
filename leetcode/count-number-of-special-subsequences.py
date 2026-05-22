#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [[0] * 3 for _ in range(2)]
        now = 0

        for i in range(n):
            x = nums[i]
            for j in range(3):
                dp[1 - now][j] = dp[now][j]

            if x == 0:
                dp[1 - now][0] += dp[now][0] + 1
            elif x == 1:
                dp[1 - now][1] += dp[now][0] + dp[now][1]
            elif x == 2:
                dp[1 - now][2] += dp[now][1] + dp[now][2]

            now = 1 - now
        ans = dp[now][2]
        return ans % MOD


true, false, null = True, False, None
cases = [
    ([0, 1, 2, 2], 3),
    ([2, 2, 0, 0], 0),
    ([0, 1, 2, 0, 1, 2], 7),
    ([2, 0, 0, 2, 0, 1, 2], 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSpecialSubsequences, cases)

if __name__ == '__main__':
    pass
