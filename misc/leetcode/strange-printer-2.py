#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        p = s[0]
        ss = []
        for c in s:
            if c != p:
                ss.append(p)
                p = c
        ss.append(p)
        print(''.join(ss))

        import functools

        @functools.lru_cache(None)
        def fun(i, j):
            if i > j:
                return 0

            ans = 1 + fun(i + 1, j)
            for k in range(i + 1, j + 1):
                if ss[i] == ss[k]:
                    ans = min(ans, fun(i + 1, k) + fun(k + 1, j))
            return ans

        ans = fun(0, len(ss) - 1)
        return ans


cases = [
    ('aaabbb', 2),
    ('aba', 2),
    ("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa", 19),
    ('abaca', 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().strangePrinter, cases)
