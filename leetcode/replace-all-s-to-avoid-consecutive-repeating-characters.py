#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def modifyString(self, s: str) -> str:
        ss = list(s)
        for i in range(len(s)):
            if ss[i] != '?': continue
            for j in range(26):
                c = chr(j + ord('a'))
                if ((i - 1) >= 0 and ss[i - 1] == c) or \
                        (((i + 1) < len(s)) and ss[i + 1] == c): continue
                ss[i] = c
                break
        ans = ''.join(ss)
        return ans
