#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        digits.sort(reverse=True)
        return digits[0] * digits[1]


if __name__ == '__main__':
    pass
