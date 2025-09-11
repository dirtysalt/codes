#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        ss = set(nums)
        d = 0
        while True:
            ans = (1 << d)
            if ans not in ss:
                return ans
            d += 1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 1], 4),
    ([5, 3, 2], 1),
]

aatest_helper.run_test_cases(Solution().minImpossibleOR, cases)

if __name__ == '__main__':
    pass
