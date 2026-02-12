#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        his = set()

        def test(i):
            if i == n:
                return len(his)

            ans = 0
            for j in range(i, n):
                if len(his) + n - j < ans: break
                ss = s[i:j + 1]
                if ss not in his:
                    his.add(ss)
                    res = test(j + 1)
                    ans = max(ans, res)
                    his.remove(ss)

            return ans

        ans = test(0)
        return ans


cases = [
    ("iedabkacb", 8),
    ('aaaaaaaaaaaaaaaa', 5),
    ("ababccc", 5),
    ("aba", 2),
    ("aa", 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxUniqueSplit, cases)
