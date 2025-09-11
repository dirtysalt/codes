#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            inc = 1
            for j in range(i, n):
                inc = inc & ((nums[j - 1] < nums[j]) if j > i else 1)
                dp[i][j] = inc

        ans = 0
        for i in range(n):
            for j in range(i, n):
                # remove nums[i..j+1]
                inc = 1
                if i > 0:
                    inc = inc & dp[0][i - 1]
                if (j + 1) < n:
                    inc = inc & dp[j + 1][n - 1]
                if i > 0 and (j + 1) < n:
                    inc = inc & (nums[i - 1] < nums[j + 1])
                ans += inc
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4], 10),
    ([6, 5, 7, 8], 7),
    ([8, 7, 6, 6], 3),
]

aatest_helper.run_test_cases(Solution().incremovableSubarrayCount, cases)

if __name__ == '__main__':
    pass
