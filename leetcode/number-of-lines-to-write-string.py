#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        max_width = 100
        rest = max_width
        cnt = 0
        for idx in range(len(S)):
            c = S[idx]
            width = widths[ord(c) - ord('a')]
            if width > rest:
                cnt += 1
                rest = max_width
            rest -= width
        cnt += 1
        return [cnt, max_width - rest]
