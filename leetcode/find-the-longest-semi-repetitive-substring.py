#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1
        for i in range(1, n):
            c = 0
            d = 0
            for j in range(i, n):
                if s[j - 1] == s[j]:
                    c += 1
                    if c >= 2:
                        d = j - i + 1
                        break
            if d == 0:
                d = n - i + 1
            ans = max(ans, d)
        return ans


if __name__ == '__main__':
    pass
