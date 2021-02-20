#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        n = len(nums)
        L = {}
        acc = 0
        for i in range(n):
            L[acc] = i
            if acc > x:
                break
            acc += nums[i]

        ans = n + 1
        acc = 0
        for i in reversed(range(n)):
            exp = x - acc
            if exp < 0: break
            if exp in L:
                op = (n - i - 1) + L[exp]
                ans = min(ans, op)
            acc += nums[i]

        if ans == (n + 1):
            ans = -1

        return ans


cases = [
    ([1, 1, 4, 2, 3], 5, 2),
    ([5, 6, 7, 8, 9], 4, -1,),
    ([3, 2, 20, 1, 1, 3], 10, 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)
