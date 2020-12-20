#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        last = {}
        ans = -1
        for i in range(len(s)):
            c = s[i]
            if c in last:
                dist = i - last[c] - 1
                ans = max(ans, dist)
            else:
                last[c] = i
        return ans
