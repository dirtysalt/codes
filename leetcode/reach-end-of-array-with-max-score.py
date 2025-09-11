#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        last = 0
        for i in range(1, n):
            if nums[i] > nums[last]:
                ans += nums[last] * (i - last)
                last = i
        ans += nums[last] * (n - 1 - last)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 3, 1, 5], 7),
    ([4, 3, 1, 3, 2], 16),
]

aatest_helper.run_test_cases(Solution().findMaximumScore, cases)

if __name__ == '__main__':
    pass
