#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = list(s)
        idx = 0

        def rev(xs, s, e):
            while s < e:
                xs[s], xs[e] = xs[e], xs[s]
                s += 1
                e -= 1

        while idx < len(s):
            if (idx + k) <= len(s):
                rev(s, idx, idx + k - 1)
            else:
                rev(s, idx, len(s) - 1)
            idx += 2 * k
        return ''.join(s)
