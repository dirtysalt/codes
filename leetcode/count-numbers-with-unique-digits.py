#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        base = 1
        for i in range(n - 1):
            base *= (9 - i)
            ans += 9 * base
        return ans
