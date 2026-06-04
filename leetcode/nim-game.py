#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n % 4 == 0:
            return False
        return True
