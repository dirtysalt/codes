#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0] * n for _ in range(2)]
        nums = [nums1, nums2]

        dp[0][0] = dp[1][0] = 1
        for i in range(1, n):
            for j in range(2):
                dp[j][i] = 1
                if nums[j][i] >= nums[j][i - 1]:
                    dp[j][i] = max(dp[j][i], dp[j][i - 1] + 1)
                if nums[j][i] >= nums[1 - j][i - 1]:
                    dp[j][i] = max(dp[j][i], dp[1 - j][i - 1] + 1)

        ans = max(max(dp[0]), max(dp[1]))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 1], [1, 2, 1], 2),
    ([1, 3, 2, 1], [2, 2, 3, 4], 4),
    ([1, 1], [2, 2], 2),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 3)
aatest_helper.run_test_cases(Solution().maxNonDecreasingLength, cases)

if __name__ == '__main__':
    pass
