#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        ps = [0] * 26
        for i in range(len(S)):
            ps[ord(S[i]) - ord('a')] = i
        t = list(T)
        t.sort(key=lambda x: ps[ord(x) - ord('a')])
        return ''.join(t)
