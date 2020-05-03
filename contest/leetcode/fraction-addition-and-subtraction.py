#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def fractionAddition(self, expression: str) -> str:
        ans = None

        def add(op1, op2):
            a, b = op1
            c, d = op2
            x = a * d + b * c
            y = b * d
            x, y = norm(x, y)
            return x, y

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def norm(x, y):
            g = gcd(x, y)
            return x // g, y // g

        i = 0
        expr = expression
        while i < len(expr):
            sign = 1
            if expr[i] in '+-':
                if expr[i] == '-':
                    sign = -1
                i += 1

            a = 0
            while i < len(expr) and expr[i].isdigit():
                a = a * 10 + (ord(expr[i]) - ord('0'))
                i += 1
            a = a * sign

            i += 1
            b = 0
            while i < len(expr) and expr[i].isdigit():
                b = b * 10 + (ord(expr[i]) - ord('0'))
                i += 1

            if ans is None:
                ans = norm(a, b)
            else:
                ans = add(ans, (a, b))

        a, b = ans
        return '%d/%d' % (a, b)
