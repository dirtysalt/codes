#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        sz = high - low + 1
        ans = sz // 2
        if sz % 2 == 1 and low % 2 == 1 and high % 2 == 1:
            ans += 1
        return ans
