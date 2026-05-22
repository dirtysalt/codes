#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        allOdd, allEven = 0, 0
        for i in range(n):
            if i % 2 == 0:
                allEven += nums[i]
            else:
                allOdd += nums[i]

        odd, even = 0, 0
        ans = 0
        for i in range(n):
            if i % 2 == 0:
                # 0 1 2 3 4(x) 5 6 7
                allEven -= nums[i]
                # allEven = [6], allOdd =[5,7]
                # even = [0,2] odd = [1,3]
                if (even + allOdd) == (odd + allEven):
                    ans += 1
                even += nums[i]
            else:
                allOdd -= nums[i]
                if (even + allOdd) == (odd + allEven):
                    ans += 1
                odd += nums[i]
        return ans


cases = [
    ([2, 1, 6, 4], 1),
    ([1, 1, 1], 3),
    ([1, 2, 3], 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().waysToMakeFair, cases)
