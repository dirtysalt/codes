#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        def isOK(t):
            c = 1
            mx = 0
            acc = 0
            for x in time:
                acc += x
                mx = max(x, mx)
                if (acc - mx) > t:
                    c += 1
                    mx = x
                    acc = x
            return c <= m

        s, e = 0, sum(time)
        while s <= e:
            t = (s + e) // 2
            if isOK(t):
                e = t - 1
            else:
                s = t + 1
        ans = s
        return ans


cases = [
    ([50, 47, 68, 33, 35, 84, 25, 49, 91, 75], 1, 466),
    ([1, 2, 3, 3], 2, 3),
    ([999, 999, 999], 4, 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minTime, cases)
