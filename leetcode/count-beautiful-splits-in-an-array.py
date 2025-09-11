#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for sz in range(1, n + 1):
            for i in reversed(range(0, n - sz + 1)):
                j = i + sz - 1
                k = dp[i + 1][j + 1] if (j + 1) < n else 0
                if nums[i] == nums[j]:
                    dp[i][j] = k + 1

        ans = 0
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if (dp[0][i] >= i and i <= (j - i)) or (dp[i][j] >= (j - i) and (j - i) <= (n - j)):
                    # print(nums[:i], nums[i:j], nums[j:])
                    # print(dp[0][i], i, dp[i][j], (j - i))
                    ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1, 2, 1], 2),
    ([1, 2, 3, 4], 0),
    ([2, 3, 2, 2, 1], 1),
    ([0, 2, 0, 2, 1, 3, 1, 0], 4),
]

aatest_helper.run_test_cases(Solution().beautifulSplits, cases)

if __name__ == '__main__':
    pass
