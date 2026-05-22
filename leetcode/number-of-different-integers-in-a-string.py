#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        values = set()

        d = -1
        for c in word:
            x = ord(c) - ord('0')
            if x >= 0 and x <= 9:
                if d == -1:
                    d = x
                else:
                    d = d * 10 + x
            else:
                values.add(d)
                d = -1

        values.add(d)
        ans = len(values)
        if -1 in values:
            ans -= 1
        return ans
