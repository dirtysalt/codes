#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        def test(value):
            res = 0
            for x in arr:
                if x > value:
                    res += value
                else:
                    res += x
            return res

        s, e = 0, max(arr)
        while s <= e:
            value = (s + e) // 2
            res = test(value)
            if res >= target:
                e = value - 1
            else:
                s = value + 1

        # test(s) >= target
        # try s and s - 1
        ans = s
        if abs(test(s) - target) >= abs(test(s - 1) - target):
            ans = s - 1
        return ans


cases = [
    ([4, 9, 3], 10, 3),
    ([2, 3, 5], 10, 5),
    ([60864, 25176, 27249, 21296, 20204], 56803, 11361)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findBestValue, cases)
