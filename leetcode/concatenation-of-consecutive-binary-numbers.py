#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        MOD = 10 ** 9 + 7

        for x in range(1, n + 1):
            x2 = x
            w = 0
            while x2:
                w += 1
                x2 = x2 // 2

            ans = (ans << w) + x
            ans = ans % MOD

        return ans
