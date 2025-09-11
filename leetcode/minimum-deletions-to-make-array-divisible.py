#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        x = numsDivide[0]
        for i in range(1, len(numsDivide)):
            x = gcd(x, numsDivide[i])

        nums.sort()
        for i in range(len(nums)):
            if x % nums[i] == 0:
                return i
        return -1


true, false, null = True, False, None
cases = [
    ([2, 3, 2, 4, 3], [9, 6, 9, 3, 15], 2),
    ([4, 3, 6], [8, 2, 6, 10], -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
