#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in reversed(range(n)):
            d = nums[i] % 2
            # jump to d
            dp[i][d] = nums[i] + dp[i + 1][d]
            # jump to 1-d
            # if dp[i + 1][1 - d] != 0:
            dp[i][d] = max(dp[i][d], dp[i + 1][1 - d] + nums[i] - x)

            dp[i][0] = max(dp[i][0], dp[i + 1][0])
            dp[i][1] = max(dp[i][1], dp[i + 1][1])

        return dp[0][nums[i] % 2]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 6, 1, 9, 2], 5, 13),
    ([2, 4, 6, 8], 3, 20),
]

aatest_helper.run_test_cases(Solution().maxScore, cases)

if __name__ == '__main__':
    pass
