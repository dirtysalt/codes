#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minInsertions(self, s: str) -> int:
        st = 0
        i, n = 0, len(s)
        ans = 0
        while i < n:
            if s[i] == '(':
                i += 1
                st += 1
                continue

            if not ((i + 1) < n and s[i + 1] == ')'):
                i += 1
                ans += 1
            else:
                i += 2

            if st <= 0:
                ans += 1
            else:
                st -= 1

        if st:
            ans += 2 * st
        return ans


cases = [
    ("(()))", 1),
    ("())", 0),
    ("))())(", 3),
    ("((((((", 12)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minInsertions, cases)
