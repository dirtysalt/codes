#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i, j = 0, len(S) - 1
        t = list(S)
        while True:
            while i <= j and not t[i].isalpha():
                i += 1
            while i <= j and not t[j].isalpha():
                j -= 1
            if i <= j:
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1
            else:
                break
        ans = ''.join(t)
        return ans
