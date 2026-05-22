#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        exp = '0'
        ans = 0
        for i in range(n):
            if target[i] == exp:
                continue

            ans += 1
            if exp == '0':
                exp = '1'
            else:
                exp = '0'
        return ans
