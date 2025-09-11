#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def calculate(self, s: str) -> int:

        st = []

        def do_muldiv(v):
            if st and st[-1] in '*/':
                op = st.pop()
                a = st.pop()
                if op == '*':
                    res = a * v
                else:
                    res = a // v
                v = res
            st.append(v)

        v = 0
        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                v = v * 10 + ord(c) - ord('0')
            else:
                do_muldiv(v)
                st.append(c)
                v = 0

        do_muldiv(v)

        ans = st[0]
        for i in range(1, len(st), 2):
            if st[i] == '+':
                ans += st[i + 1]
            else:
                ans -= st[i + 1]
        return ans


import aatest_helper

cases = [
    ("3+2*2", 7),
    (" 3+5 / 2 ", 5),
    (" 3/2 ", 1),
    ('1-1+1', 1)
]

aatest_helper.run_test_cases(Solution().calculate, cases)
