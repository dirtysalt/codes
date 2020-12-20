#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        hs = [0] * n  # 其实可以不用分配这个空间
        P = 10 ** 9 + 7
        mul = 31  # 选择一个质数可能会好点

        base = 1
        h = 0
        for i in reversed(range(1, n)):
            h += base * (ord(s[i]) - ord('a'))
            h = h % P
            hs[i] = h
            base = (base * mul) % P

        h = 0
        ans = -1
        for i in range(n - 1):
            j = n - 1 - i
            h = h * mul + (ord(s[i]) - ord('a'))
            h = h % P
            if hs[j] == h and s[:i + 1] == s[-(i + 1):]:
                ans = i

        ans = s[:ans + 1]
        return ans
