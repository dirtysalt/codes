#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        P, N = -1, -1
        acc = 1
        ans = 0
        for i in range(n):
            x = nums[i]
            if x == 0:
                acc = 1
                P, N = i, -1
                continue

            if x < 0:
                acc = -acc
                if N < 0: N = i

            if acc > 0:
                ans = max(ans, i - P)
            if acc < 0:
                if N >= 0: ans = max(ans, i - N)
        return ans


cases = [
    ([1, -2, -3, 4], 4),
    ([0, 1, -2, -3, -4], 3),
    ([-1, -2, -3, 0, 1], 2),
    ([-1, 2], 1),
    ([1, 2, 3, 5, -6, 4, 0, 10], 4),
    ([-1, -1], 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getMaxLen, cases)
