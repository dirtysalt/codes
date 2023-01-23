#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        ok = False
        for c in s:
            if c != ' ':
                ok = True
            else:
                if ok:
                    ans += 1
                ok = False
        if ok:
            ans += 1
        return ans
