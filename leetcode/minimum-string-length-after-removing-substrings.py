#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for c in s:
            st.append(c)
            if ''.join(st[-2:]) in ('AB', 'CD'):
                st.pop()
                st.pop()
        return len(st)


if __name__ == '__main__':
    pass
