#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        v = 0
        y = x
        while x:
            r = x % 10
            x = x / 10
            v = v * 10 + r
        return v == y
