#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import Counter
        dp = [Counter() for _ in range(2)]
        dp[0][0] = 1
        now = 0

        for i in range(n):
            dp[1 - now] = dp[now].copy()

            x = nums[i]
            for st, c in dp[now].items():
                dp[1 - now][st | x] += c
            now = 1 - now

        M = max(dp[now].keys())
        return dp[now][M]


true, false, null = True, False, None
cases = [
    ([36054, 31062, 5349, 79034, 65321, 33621, 49162, 45464, 8011, 83322, 72357, 85884], 3165),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countMaxOrSubsets, cases)

if __name__ == '__main__':
    pass
