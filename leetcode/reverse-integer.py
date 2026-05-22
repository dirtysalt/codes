#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        neg = False
        if x[0] in ('-', '+'):
            if x[0] == '-': neg = True
            x = x[1:]
        x = x[::-1]
        v = int(x)
        if neg:
            v = -v
            if v < -(1 << 31):
                v = 0
        elif v > (1 << 31) - 1:
            v = 0
        return v
