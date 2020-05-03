#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        st = [0] * (n + 1)
        st[0] = 1
        for i in range(1, n + 1):
            v = 0
            for j in range(0, i):
                v += st[j] * st[i - 1 - j]
            st[i] = v
        return st[n]
