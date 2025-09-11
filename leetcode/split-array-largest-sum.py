#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = 0
                ans = -1
                for k in reversed(range(1, i + 1)):
                    s += nums[k - 1]
                    res = dp[k - 1][j - 1]

                    # invalid state
                    if res == -1:
                        continue

                    # prune search
                    if ans != -1 and s >= ans:
                        break

                    v = max(s, res)
                    if ans == -1:
                        ans = v
                    else:
                        ans = min(ans, v)
                dp[i][j] = ans
        ans = dp[n][m]
        return ans


cases = [
    ([7, 2, 5, 10, 8], 2, 18)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().splitArray, cases)
