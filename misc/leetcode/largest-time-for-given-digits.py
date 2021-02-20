#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def parse(x):
            a = x[0] * 10 + x[1]
            b = x[2] * 10 + x[3]
            # print(a, b)
            if 0 <= a < 24 and 0 <= b < 60:
                return True, a * 60 + b
            else:
                return False, None

        import itertools
        ans = -1
        p = None
        for x in itertools.permutations(A):
            ok, t = parse(x)
            if ok and t > ans:
                ans = t
                p = x

        if p is None:
            return ""
        ans = "%d%d:%d%d" % (p[0], p[1], p[2], p[3])
        return ans


cases = [
    ([1, 2, 3, 4], "23:41"),
    ([5, 5, 5, 5], ""),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestTimeFromDigits, cases)
