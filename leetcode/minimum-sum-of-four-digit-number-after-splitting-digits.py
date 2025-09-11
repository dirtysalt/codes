#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumSum(self, num: int) -> int:

        ans = 1 << 30
        ds = []
        while num:
            ds.append(num % 10)
            num = num // 10
        ds.sort(reverse=True)

        a, b = 0, 0
        while ds:
            a = a * 10 + ds.pop()
            if ds:
                b = b * 10 + ds.pop()

        return a + b


if __name__ == '__main__':
    pass
