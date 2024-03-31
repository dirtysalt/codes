#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def f(x):
            r = 0
            while x:
                r += x % 10
                x = x // 10
            return r

        r = f(x)
        if x % r == 0: return r
        return -1


if __name__ == '__main__':
    pass
