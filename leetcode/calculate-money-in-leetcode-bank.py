#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        s = 1
        while n >= 7:
            ans += s * 7 + 21
            n -= 7
            s += 1

        while n:
            ans += s
            s += 1
            n -= 1
        return ans
