#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        def test(t):
            j = 0
            res = 0
            for i in range(n):
                if bloomDay[i] > t:
                    j = i + 1
                else:
                    if (i - j + 1) == k:
                        res += 1
                        j = i + 1
            return res >= m

        s, e = 1, max(bloomDay)
        while s <= e:
            t = (s + e) // 2
            if test(t):
                e = t - 1
            else:
                s = t + 1
        ans = s
        return ans


cases = [
    ([1, 10, 3, 10, 2], 3, 1, 3),
    ([1, 10, 3, 10, 2], 3, 2, -1),
    ([7, 7, 7, 7, 12, 7, 7], 2, 3, 12),
    ([1000000000, 1000000000], 1, 1, 1000000000),
    ([1, 10, 2, 9, 3, 8, 4, 7, 5, 6], 4, 2, 9),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDays, cases)
