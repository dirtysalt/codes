#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(1 << 31):
            if divisor == -1:
                # overflow
                return (1 << 31) - 1

        if dividend == 0:
            return 0

        neg = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg = 1
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        ans = 0
        while dividend >= divisor:
            y = divisor
            t = 1
            while (y + y) < dividend:
                y = y + y
                t = t + t
            ans += t
            dividend -= y

        if neg:
            ans = -ans
        return ans
