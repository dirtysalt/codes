#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 5
        res = 0
        while (k <= n):
            res += n // k
            k = k * 5
        return res
