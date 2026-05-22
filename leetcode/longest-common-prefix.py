#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        s = strs[0]
        for i in range(len(s), 0, -1):
            ps = s[:i]
            match = True
            for x in strs:
                if not x.startswith(ps):
                    match = False
                    break
            if match: return ps
        return ''
