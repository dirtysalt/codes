#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        A = [0] * 26
        B = [0] * 26
        for c in a:
            A[ord(c) - ord('a')] += 1
        for c in b:
            B[ord(c) - ord('a')] += 1

        ans = 1 << 25
        for i in range(26):
            op = len(a) + len(b) - A[i] - B[i]
            ans = min(ans, op)

        for i in range(1, 26):
            A[i] += A[i - 1]
            B[i] += B[i - 1]

        for s1 in range(26):
            for s2 in range(s1 + 1, 26):
                ca = len(a) - A[s1]
                cb = B[s2 - 1]
                op = ca + cb

                ca = A[s2 - 1]
                cb = len(b) - B[s1]
                op2 = ca + cb

                ans = min(ans, op, op2)
        return ans


cases = [
    ("aba", "caa", 2),
    ("dabadd", "cda", 3),
    ('d', 'c', 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCharacters, cases)
