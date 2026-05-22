#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n:
            x = (n - 1) % 26
            n = (n - 1) // 26
            ans.append(chr(x + ord('A')))
        return ''.join(ans[::-1])
