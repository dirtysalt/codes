#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return 2 * n


if __name__ == '__main__':
    pass
