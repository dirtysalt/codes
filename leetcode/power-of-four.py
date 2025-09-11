#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        for i in range(0, 31, 2):
            mask = 1 << i
            if ((num >> i) & 0x1) and ((num & ~mask) == 0):
                return True
        return False
