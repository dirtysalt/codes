#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a, b = [0] * n, [0] * n

        x = 0
        for i in reversed(range(n)):
            if s[i] == 'a':
                x += 1
            a[i] = x
        x = 0
        for i in range(n):
            if s[i] == 'b':
                x += 1
            b[i] = x

        ans = n
        for i in range(n):
            op = b[i] + a[i] - 1
            ans = min(ans, op)
        return ans
