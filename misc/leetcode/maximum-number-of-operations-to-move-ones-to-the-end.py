#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        st, i = 0, 0
        while i < len(s):
            if s[i] == '0':
                ans += st
                while i < len(s) and s[i] == '0': i += 1
            else:
                st += 1
                i += 1
        return ans


if __name__ == '__main__':
    pass
