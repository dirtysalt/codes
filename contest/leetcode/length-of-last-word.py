#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        s = s.strip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                cnt += 1
            else:
                break
        return cnt
