#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countHomogenous(self, s: str) -> int:

        def test(sz):
            # print(sz)
            return sz * (sz + 1) // 2

        n = len(s)
        j = 0
        ans = 0
        for i in range(n):
            if s[i] == s[j]: continue
            sz = i - j
            ans += test(sz)
            j = i
        ans += test(n - j)
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans
