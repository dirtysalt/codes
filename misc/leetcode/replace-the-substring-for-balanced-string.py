#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def balancedString(self, s: str) -> int:

        def ch2int(c):
            if c == 'Q':
                return 0
            elif c == 'W':
                return 1
            elif c == 'E':
                return 2
            else:
                return 3

        s = [ch2int(c) for c in s]
        exp = [0] * 4
        n = len(s)
        avg = n // 4

        for c in s:
            exp[c] += 1
        for i in range(4):
            if exp[i] >= avg:
                exp[i] -= avg
            else:
                exp[i] = 0
        if all([x == 0 for x in exp]):
            return 0

        print(exp)
        st = [0] * 4

        def is_ok():
            for i in range(4):
                if exp[i] > 0 and st[i] < exp[i]:
                    return False
            return True

        ans = n
        j = 0
        for i in range(n):
            c = s[i]
            st[c] += 1
            if is_ok():
                while j <= i and is_ok():
                    st[s[j]] -= 1
                    j += 1
                ans = min(ans, i - j + 2)
        return ans


cases = [
    ('QWER', 0),
    ('QQQW', 2),
    ('EQQR', 1),
    ("WQWRQQQW", 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().balancedString, cases)
