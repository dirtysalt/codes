#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        c = len([x for x in s if x == '1'])
        ans = '1' * (c - 1) + '0' * (n - c) + '1'
        return ans


if __name__ == '__main__':
    pass
