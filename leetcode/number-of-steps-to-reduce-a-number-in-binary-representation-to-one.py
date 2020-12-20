#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        c = 0
        for i in reversed(range(0, len(s))):
            v = ord(s[i]) - ord('0')
            v += c
            if i == 0 and v == 1:
                break

            if v == 0:
                ans += 1
                c = 0
            elif v == 1:
                ans += 2
                c = 1
            else:
                ans += 1
                c = 1
        return ans
