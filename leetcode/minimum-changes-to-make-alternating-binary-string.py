#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minOperations(self, s: str) -> int:

        def test(exp):
            ans = 0
            for c in s:
                if ord(c) - ord('0') != exp:
                    ans += 1
                exp = 1 - exp
            return ans

        a = test(0)
        b = test(1)
        return min(a, b)
