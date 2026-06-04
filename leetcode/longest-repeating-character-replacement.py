#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        for _c in range(26):
            c = chr(_c + ord('A'))
            kk = k
            j = 0
            for i in range(n):
                if s[i] == c:
                    ans = max(ans, i - j + 1)
                    continue

                while j <= i and kk <= 0:
                    if s[j] != c:
                        kk += 1
                    j += 1
                kk -= 1
                ans = max(ans, i - j + 1)
        return ans
