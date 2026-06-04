#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(n):
            mark = [0] * 26
            for j in range(i, n):
                c = s[j]
                c2 = ord(c)
                if c2 >= ord('A') and c2 <= ord('Z'):
                    c2 -= ord('A')
                    mark[c2] |= 1
                else:
                    c2 -= ord('a')
                    mark[c2] |= 2
                ok = True
                for x in mark:
                    if x != 0 and x != 3:
                        ok = False
                        break
                if ok and (j - i + 1) > len(ans):
                    ans = s[i:j + 1]
        return ans
