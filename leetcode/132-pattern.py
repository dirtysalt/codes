#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        ks = []
        ks.append(nums[-1])
        js = [None] * n

        def largest_but_less(ks, x):
            s, e = 0, len(ks) - 1
            while s <= e:
                m = (s + e) // 2
                if ks[m] >= x:
                    e = m - 1
                else:
                    s = m + 1
            # query e
            if e >= 0:
                ans = ks[e]
            else:
                ans = None
            ks.insert(e + 1, x)
            # print(ks)
            return ans

        for i in reversed(range(n - 1)):
            x = nums[i]
            y = largest_but_less(ks, x)
            js[i] = y

        # print(js)
        min_value = nums[0]
        for i in range(n - 2):
            min_value = min(min_value, nums[i])
            if js[i + 1] is not None and min_value < js[i + 1]:
                return True

        return False


cases = [
    ([3, 1, 4, 2], True),
    ([1, 2, 3, 4, ], False),
    ([-1, 3, 2, 0], True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().find132pattern, cases)
