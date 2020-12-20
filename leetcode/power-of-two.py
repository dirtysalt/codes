#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isPowerOfTwo(self, num):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0, 31, 1):
            mask = 1 << i
            if ((num >> i) & 0x1) and ((num & ~mask) == 0):
                return True
        return False
