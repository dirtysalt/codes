#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        def check_chunk(ck, ps):
            for i in range(1, ps):
                if s[:ck] != s[i * ck: (i+1) * ck]:
                    return False
            return True

        for ps in range(2, n+1):
            if n % ps == 0:
                ck = n // ps
                if check_chunk(ck, ps):
                    return True
        
        return False

import aatest_helper

cases = [
    ("abab", True),
    ("aba", False),
    ("abcabcabcabc", True),
    ("abcdefghijklmnopqrstuvw123" * 300, True)
]

aatest_helper.run_test_cases(Solution().repeatedSubstringPattern, cases)