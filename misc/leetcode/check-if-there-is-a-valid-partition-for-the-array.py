#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            if dp[i] == 0: continue
            x = nums[i]
            if (i + 1) < n and nums[i + 1] == x:
                dp[i + 2] = 1
            if (i + 2) < n and nums[i + 1] == nums[i + 2] == x:
                dp[i + 3] = 1
            if (i + 2) < n and nums[i + 1] == (x + 1) and nums[i + 2] == (x + 2):
                dp[i + 3] = 1

        return bool(dp[n])


true, false, null = True, False, None
cases = [
    ([4, 4, 4, 5, 6], true),
    ([1, 1, 1, 2], false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().validPartition, cases)

if __name__ == '__main__':
    pass
