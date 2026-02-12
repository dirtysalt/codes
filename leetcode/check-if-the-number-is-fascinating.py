#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isFascinating(self, n: int) -> bool:
        c = [0] * 10

        def mark(x):
            while x:
                c[x % 10] += 1
                x = x // 10

        mark(n)
        mark(n * 2)
        mark(n * 3)
        for i in range(1, 10):
            if c[i] != 1:
                return False
        return True


if __name__ == '__main__':
    pass
