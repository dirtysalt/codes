#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def splitNum(self, num: int) -> int:
        ds = []
        while num > 0:
            ds.append(num % 10)
            num = num // 10
        ds.sort()

        i, a, b = 0, 0, 0
        while i < len(ds):
            a = a * 10 + ds[i]
            if (i + 1) < len(ds):
                b = b * 10 + ds[i + 1]
            i += 2
        return a + b


if __name__ == '__main__':
    pass
