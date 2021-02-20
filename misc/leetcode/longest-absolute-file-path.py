#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        st = []
        sz = 0

        i = 0
        t = 0
        ans = 0
        dot = False
        while i < len(input):
            c = input[i]
            i += 1
            if c == '\n':
                st.append(t + 1)
                sz += st[-1]

                t = 0
                tabs = 0
                dot = False
                while i < len(input) and input[i] == '\t':
                    tabs += 1
                    i += 1

                while len(st) > tabs:
                    sz -= st[-1]
                    st.pop()
            else:
                t += 1
                if c == '.':
                    dot = True
                if dot:
                    ans = max(ans, sz + t)
        return ans


cases = [
    ('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext', 20),
    ('a', 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().lengthLongestPath, cases)
