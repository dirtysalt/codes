#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reverseVowels(self, s: str) -> str:
        ss = list(s)
        n = len(ss)
        pos = [i for i in range(n) if ss[i] in 'aeoiuAEIOU']
        i, j = 0, len(pos) - 1
        while i <= j:
            x, y = pos[i], pos[j]
            ss[x], ss[y] = ss[y], ss[x]
            i += 1
            j -= 1
        ans = ''.join(ss)
        return ans
