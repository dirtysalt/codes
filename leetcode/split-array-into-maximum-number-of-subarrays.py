#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans = 0
        prev = 0
        for x in nums:
            if not prev:
                prev = x
            else:
                prev = prev & x
            if not prev:
                ans += 1
        if prev and ans == 0:
            ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 0, 2, 0, 1, 2], 3),
    ([5, 7, 1, 3], 1),
    ([1, 2, 2, 1], 2)
]

aatest_helper.run_test_cases(Solution().maxSubarrays, cases)

if __name__ == '__main__':
    pass
