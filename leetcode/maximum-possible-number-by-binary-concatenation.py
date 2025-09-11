#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import itertools
from typing import List


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        def tobin(x):
            return bin(x)[2:]

        arr = [tobin(x) for x in nums]
        ans = 0
        for x in itertools.permutations(arr):
            r =  int(''.join(x), 2)
            ans = max(ans, r)
        return ans

true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 30),
    ([2, 8, 16], 1296),
]

aatest_helper.run_test_cases(Solution().maxGoodNumber, cases)

if __name__ == '__main__':
    pass
