#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        for op in path.split('/'):
            if op == '' or op == '.':
                pass

            elif op == '..':
                if st:
                    st.pop()

            else:
                st.append(op)

        ans = '/' + '/'.join(st)
        return ans
