#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def flip(x):
            ss = []
            while x:
                ss.append(x % 10)
                x = x // 10
            t = 0
            for x in ss:
                t = t * 10 + x
            return t

        for x in range(num + 1):
            y = flip(x)
            if x + y == num:
                return True
        return False


if __name__ == '__main__':
    pass
