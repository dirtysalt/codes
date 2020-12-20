#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x <= 3: return 1
        s, e = 1, x / 2
        while s <= e:
            m = (s + e) / 2
            v = m * m
            if v == x:
                return m
            elif v > x:
                e = m - 1
            else:
                s = m + 1
        return e
