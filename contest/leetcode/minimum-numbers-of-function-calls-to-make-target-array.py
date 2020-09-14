#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        while True:
            allZero = True
            for x in nums:
                if x % 2 == 1:
                    ans += 1
                    x = x - 1
                if x != 0:
                    allZero = False
            if allZero: break
            nums = [x // 2 for x in nums]
            ans += 1
        return ans


cases = [
    ([1, 5], 5),
    ([2, 2], 3),
    ([4, 2, 5], 6),
    ([3, 2, 2, 4], 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)
