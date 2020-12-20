#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        tmp = [x[::-1] for x in ss]
        ans = ' '.join(tmp)
        ans = ans[::-1]
        return ans
