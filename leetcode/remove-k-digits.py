#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        for i in range(n):
            c = num[i]

            while k > 0 and st and c < st[-1]:
                st.pop()
                k -= 1

            st.append(c)

        while k > 0 and st:
            st.pop()
            k -= 1

        ans = ''.join(st)
        ans = ans.lstrip('0')
        ans = ans or '0'
        return ans
