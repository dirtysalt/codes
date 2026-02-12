#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        res = 0
        A = 10 ** 4
        if length >= A or width >= A or height >= A or mass >= A:
            res |= 2
        v = length * width * height
        if v >= 10 ** 9:
            res |= 2
        if mass >= 100:
            res |= 1
        values = ['Neither', 'Heavy', 'Bulky', 'Both']
        return values[res]


if __name__ == '__main__':
    pass
