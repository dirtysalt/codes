#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def count(s):
            res = 0
            for c in s.lower():
                if c in 'aeiou':
                    res += 1
            return res

        a = count(s[:len(s) // 2])
        b = count(s[len(s) // 2:])
        return a == b
