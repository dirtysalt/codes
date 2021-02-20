#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPar(s):
            return s == s[::-1]

        def ok(a, b):
            n = len(a)
            i, j = 0, n - 1
            while i <= j and a[i] == b[j]:
                i += 1
                j -= 1
            if i >= j:
                return True
            ax = a[i:j + 1]
            by = b[i:j + 1]
            # print(ax, by)
            if isPar(ax) or isPar(by):
                return True
            return False

        if ok(a, b) or ok(b, a):
            return True
        return False


class Solution2:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPar(s):
            return s == s[::-1]

        n = len(a)
        for i in range(n + 1):
            ax, ay = a[:i], a[i:]
            bx, by = b[:i], b[i:]
            if isPar(ax + by) or isPar(bx + ay):
                print(ax, by)
                return True
        return False


cases = [
    ("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp", True),
    ("aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea", True),
    ("xbdef", "xecab", False),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkPalindromeFormation, cases)
