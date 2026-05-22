#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j and s[i] == s[j]:
            i2 = i + 1
            while i2 <= j and s[i2] == s[i]: i2 += 1
            j2 = j - 1
            while i2 <= j2 and s[j2] == s[j]: j2 -= 1
            i = i2
            j = j2
        ans = max(j - i + 1, 0)
        return ans


cases = [
    ("ca", 2),
    ("cabaabac", 0),
    ("aabccabba", 3),
    ("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb", 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumLength, cases)
