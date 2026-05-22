#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """

    def findTheDifference(self, s, t):
        # Write your code here

        count = [0] * 26
        for x in s:
            count[ord(x) - ord('a')] += 1
        for x in t:
            idx = ord(x) - ord('a')
            if count[idx] == 0:
                break
            count[idx] -= 1
        return x