#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num) - 1
        while num[n] == '0':
            n -= 1
        return num[:n + 1]


if __name__ == '__main__':
    pass
