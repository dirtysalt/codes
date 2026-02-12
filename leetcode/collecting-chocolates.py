#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        MIN = min(nums)
        MAX = max(nums)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][0] = nums[i]
        for k in range(1, n):
            for i in range(n):
                dp[i][k] = min(dp[(i + 1) % n][k - 1], nums[i])

        ans = MAX * n + (n - 1) * x
        for k in range(n):
            if ans <= (MIN * n) + k * x: continue
            res = k * x
            for i in range(n):
                res += dp[i][k]
            ans = min(ans, res)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([20, 1, 15], 5, 13),
    ([1, 2, 3], 4, 6),
]

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
