#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        s, e = 1, int((2 * n) ** 0.5) + 1
        while s <= e:
            m = (s + e) // 2
            v = (m + 1) * m // 2
            if v > n:
                e = m - 1
            else:
                s = m + 1
        return e
