#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n = numBottles
        empty = 0
        ans = 0
        while n > 0:
            ans += n
            x = n + empty
            n = x // numExchange
            empty = x % numExchange
        return ans
