#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []

        p = s[0]
        cnt = 0

        def update(p, cnt):
            # print(p, cnt)
            cnt = cnt % k

            while st:
                (a, b) = st[-1]
                if a != p:
                    break
                cnt = (cnt + b) % k
                st.pop()

            if cnt:
                st.append((p, cnt))

        for c in s:
            if c == p:
                cnt += 1
            else:
                update(p, cnt)
                p = c
                cnt = 1
        update(p, cnt)
        ans = ''.join([x[0] * x[1] for x in st])
        return ans


cases = [
    ("deeedbbcccbdaa", 3, "aa"),
    ("pbbcggttciiippooaais", 2, "ps"),
    ("abcd", 2, "abcd")
]
import aatest_helper

aatest_helper.run_test_cases(Solution().removeDuplicates, cases)
