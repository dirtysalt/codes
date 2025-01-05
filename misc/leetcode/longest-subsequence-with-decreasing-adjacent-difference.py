#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # dp[x][y] 表示结尾是x, 并且差值是y的最大长度
        N = max(nums)
        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for x in nums:
            for y in range(N + 1):
                z = abs(x - y)
                dp[x][z] = max(dp[x][z], dp[y][z] + 1)

            dp[x][x] = max(dp[x][x], 1)

            for z in reversed(range(N)):
                dp[x][z] = max(dp[x][z], dp[x][z + 1])

            # print(dp[x])

        ans = 1
        for x in range(N + 1):
            ans = max(ans, max(dp[x]))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 1], 3),
    ([4, 2, ], 2),
    ([6, 5, 3, 4, 2, 1], 4),
    ([10, 20, 10, 19, 10, 20], 5)
]

aatest_helper.run_test_cases(Solution().longestSubsequence, cases)

if __name__ == '__main__':
    pass
