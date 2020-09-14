#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        p = 1
        while p * p <= n:
            p += 1
        p -= 1
        return p
