#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def pivotInteger(self, n: int) -> int:
        tt = sum(range(1, n + 1))
        acc = 0
        for x in range(1, n + 1):
            acc += x
            if (tt - acc + x) == acc:
                return x
        return -1


if __name__ == '__main__':
    pass
