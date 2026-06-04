#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split()
        n = len(ss)
        ans = [''] * n

        for c in ss:
            idx = int(c[-1])
            c = c[:-1]
            ans[idx - 1] = c

        return " ".join(ans)
