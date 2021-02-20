#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        a, b = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 + c2 == 'xy':
                a += 1
            elif c1 + c2 == 'yx':
                b += 1

        if a % 2 != b % 2:
            return -1

        ans = a // 2 + b // 2
        ans += (a % 2) * 2
        return ans


cases = [
    ("xxyyxyxyxx", "xyyxyxxxyx", 4),
    ("xx", "yy", 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumSwap, cases)
