#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        d = 0
        for c in s:
            if c == '(':
                d += 1
                ans = max(ans, d)
            elif c == ')':
                d -= 1
            else:
                pass
        return ans
