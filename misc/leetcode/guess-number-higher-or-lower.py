#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            m = (s + e) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == -1:
                e = m - 1
            else:
                s = m + 1
        raise Exception("Something wrong")
