#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = list(s)
        start = 0
        while True:
            # skip white space.
            while start < len(s) and s[start] == ' ':
                start += 1
            if start == len(s):
                break
            begin = start
            while start < len(s) and s[start] != ' ':
                start += 1
            end = start - 1
            while begin < end:
                s[begin], s[end] = s[end], s[begin]
                begin += 1
                end -= 1
        return ''.join(s)
