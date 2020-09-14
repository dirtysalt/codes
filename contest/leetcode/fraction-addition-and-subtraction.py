#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def fractionAddition(self, expression: str) -> str:

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def add(x, y, a, b):
            xx = b * x + a * y
            yy = y * b
            _gcd = gcd(xx, yy)
            return xx // _gcd, yy // _gcd

        def parse_int(expr, i):
            v = 0
            while i < len(expr) and expr[i].isdigit():
                v = v * 10 + int(expr[i])
                i += 1
            return v, i

        i = 0
        x, y = 0, 1

        while i < len(expression):
            sign = 1
            if expression[i] in '+-':
                if expression[i] == '-':
                    sign = -1
                i += 1

            a, i = parse_int(expression, i)
            b, i = parse_int(expression, i + 1)
            a = a * sign
            x, y = add(x, y, a, b)
        return "{}/{}".format(x, y)
