#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def toGoatLatin(self, S: str) -> str:
        ss = S.split()
        ans = []

        for i, x in enumerate(ss):
            t = x
            if t[0].lower() not in 'aeiou':
                t = t[1:] + t[0]
            t = t + 'ma' + 'a' * (i + 1)
            ans.append(t)

        ans = ' '.join(ans)
        return ans
