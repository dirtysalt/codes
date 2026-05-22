#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isdigit():
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


if __name__ == '__main__':
    pass
