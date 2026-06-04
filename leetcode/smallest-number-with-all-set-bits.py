#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def smallestNumber(self, n: int) -> int:
        b = 1
        while True:
            x = (1 << b) - 1
            if x >= n:
                return x
            b += 1


if __name__ == '__main__':
    pass
