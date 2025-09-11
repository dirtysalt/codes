#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        D = ord('a') - ord('A')
        for c in s:
            meet = False
            if st:
                c2 = st[-1]
                a = ord(c)
                b = ord(c2)
                if abs(a - b) == D:
                    meet = True
            if meet:
                st.pop()
            else:
                st.append(c)
        ans = ''.join(st)
        return ans
