#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        t = 0
        for x in nums:
            t = t ^ x

        x = t
        diff_bit = 0
        while x:
            if x & 0x1:
                break
            diff_bit += 1
            x >>= 1

        t2 = 0
        for x in nums:
            if x & (1 << diff_bit):
                t2 = t2 ^ x

        ans = [t2, t2 ^ t]
        return ans


cases = [
    ([1, 2, 1, 3, 2, 5], [3, 5])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().singleNumber, cases)
