#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     reciprocal = 0
    #     if n < 0:
    #         reciprocal = 1
    #         n = -n
    #
    #     t = x
    #     ans = 1.0
    #     while n:
    #         if n % 2 == 1:
    #             ans *= t
    #         t = t * t
    #         n = n // 2
    #
    #     if reciprocal:
    #         ans = 1.0 / ans
    #     return ans

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -n

        t = x
        ans = 1.0
        while n:
            if n % 2 == 1:
                ans *= t
            t = t * t
            n = n // 2
        return ans
