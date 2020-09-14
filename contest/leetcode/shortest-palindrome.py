#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def shortestPalindrome(self, s: str) -> str:

        n = len(s)
        for j in reversed(range(n)):
            a, b = s[:j + 1], s[j + 1:]
            if a == a[::-1]:
                ans = b[::-1] + s
                return ans

        ans = s[::-1] + s
        return ans

