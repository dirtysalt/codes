#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n = len(weights)

        def ok(m):
            d = 0
            res = 0
            for i in range(n):
                if (res + weights[i]) > m:
                    d += 1
                    res = weights[i]
                else:
                    res += weights[i]
            d += 1
            return d <= D

        s, e = max(weights), sum(weights)
        while s <= e:
            m = (s + e) // 2
            if ok(m):
                e = m - 1
            else:
                s = m + 1
        return s


cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
    ([1, 2, 3, 1, 1], 4, 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shipWithinDays, cases)
