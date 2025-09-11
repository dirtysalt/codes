#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a, b = 'a', 'b'
        if A < B:
            a, b = b, a
            A, B = B, A

        if A >= 2 * B:
            ans = (a + a + b) * B + a * (A - 2 * B)
            assert (A - 2 * B) < 3
            return ans

        # aab m
        # ab n
        # 2m + n = A
        # m + n = B
        m = A - B
        n = B - m
        ans = (a + a + b) * m + (a + b) * n
        return ans
