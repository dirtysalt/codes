#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ''

        par = [[0] * n for _ in range(n)]
        ans = ''
        for sz in range(1, n + 1):
            for i in range(0, n - sz + 1):
                j = i + sz - 1
                if s[i] == s[j]:
                    if (i + 1) > (j - 1) or par[i + 1][j - 1]:
                        par[i][j] = 1
                        ans = s[i:j + 1]
        return ans
