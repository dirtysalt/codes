#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        inf = 1 << 30
        SZ = 1 << n
        dp = [(inf, '') for _ in range(SZ)]
        for i in range(n):
            dp[1 << i] = len(A[i]), A[i]

        def common(a, b):
            res = a + b
            for k in reversed(range(1, min(len(a), len(b)) + 1)):
                if a[-k:] == b[:k]:
                    res = a + b[k:]
                    break
            return res

        for st in range(SZ):
            for i in range(n):
                if st & (1 << i) or dp[st][0] == inf:
                    continue
                a = dp[st][1]
                b = A[i]

                c = common(a, b)
                d = common(b, a)
                res = c if len(c) < len(d) else d
                st2 = st | (1 << i)
                if len(res) < dp[st2][0]:
                    dp[st2] = len(res), res

        sz, ans = dp[SZ - 1]
        # print(sz)
        return ans


cases = [
    (["alex", "loves", "leetcode"], "alexlovesleetcode"),
    (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "gctaagttcatgcatc"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shortestSuperstring, cases, eqfn=lambda x, y: len(x) == len(y))
