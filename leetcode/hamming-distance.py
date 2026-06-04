#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        ans = 0
        for i in range(32):
            if z & (1 << i):
                ans += 1
        return ans
