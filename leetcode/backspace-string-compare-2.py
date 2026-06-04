#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        n, m = len(S), len(T)
        i, j = n - 1, m - 1

        def reduce(s, i):
            x = 0
            while i >= 0 and (s[i] == '#' or x > 0):
                if s[i] == '#':
                    x += 1
                else:
                    x -= 1
                i -= 1
            return i

        while True:
            i = reduce(S, i)
            j = reduce(T, j)
            if i < 0 and j < 0:
                break

            elif i < 0 or j < 0:
                return False

                # print(i, j)
            if S[i] == T[j]:
                i -= 1
                j -= 1
            else:
                return False
        return True


cases = [
    ("nzp#o#g", "b#nzp#o#g", True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().backspaceCompare, cases)
