#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        n = len(s)
        fixed = False
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                fixed = True
                break

        if not fixed:
            # 几乎都是a.
            if n == 1:
                return ""
            s[n - 1] = 'b'

        ans = ''.join(s)
        return ans


cases = [
    ("abccba", "aaccba"),
    ("a", "")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().breakPalindrome, cases)
