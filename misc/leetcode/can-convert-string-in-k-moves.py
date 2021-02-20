#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t): return False
        changes = [0] * 26
        for i in range(len(s)):
            d = ord(t[i]) - ord(s[i]) + 26
            d = d % 26
            changes[d] += 1

        for i in range(1, 26):
            c = changes[i]
            exp = (c - 1) * 26 + i
            if exp > k: return False

        return True


cases = [
    ("input", "ouput", 9, True),
    ("abc", "bcd", 10, False),
    ("aab", "bbb", 27, True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canConvertString, cases)
