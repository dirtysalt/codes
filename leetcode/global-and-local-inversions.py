#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
一旦abs(A[i] - i) > 1的话，假设
[....,i+2,i+1,i...]这样的话，那么
local-inv就有i+2,i+1以及i+1,i 2个
而global-inv就只有1个.
"""


class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True
