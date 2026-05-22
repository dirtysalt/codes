#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num != 1:
            match = False
            for p in (2, 3, 5):
                if num % p == 0:
                    match = True
                    num /= p
                    break
            if not match:
                return False
        return True
