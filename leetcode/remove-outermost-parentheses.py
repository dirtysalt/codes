#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        st = []
        d = 0
        ans = ''
        for c in S:
            if c == '(':
                d += 1
                st.append(c)
            elif c == ')':
                d -= 1
                st.append(c)
                if d == 0:
                    ans += ''.join(st[1:-1])
                    st.clear()

        if st:
            ans += ''.join(st[1:-1])
        return ans
