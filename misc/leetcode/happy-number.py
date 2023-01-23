#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isHappy(self, n: int) -> bool:
        def value(x):
            res = 0
            while x:
                y = x % 10
                res += y * y
                x = x // 10
            return res

        visited = set()
        while n != 1:
            if n in visited:
                break
            visited.add(n)
            n = value(n)
        return n == 1
