#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import aatest_helper
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                z = nums[i] * nums[j]
                cnt[z] += 1

        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                z = nums[i] * nums[j]
                ans += cnt[z] - 1

        # c * d -> a * b
        # but to exclude c * d
        # which means a, b, c, d
        # b, a, c, d
        # a, b, d, c
        # b, a, c, d
        return ans * 4


cases = [
    ([2, 3, 4, 6], 8),
    ([1, 2, 4, 5, 10], 16),
    ([2, 3, 4, 6, 8, 12], 40),
    ([2, 3, 5, 7], 0)
]

aatest_helper.run_test_cases(Solution().tupleSameProduct, cases)
