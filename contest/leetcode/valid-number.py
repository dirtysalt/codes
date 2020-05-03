#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s: return False

        if s[0] in '+-':
            s = s[1:]
        # exponential.
        ss = s.split('e', 1)
        if len(ss) == 2:
            exp = ss[1]
            if not exp:
                return False
            if exp[0] in '+-':
                exp = exp[1:]
            if not exp.isdigit():
                return False
        s = ss[0]
        # fractional.
        ss = s.split('.', 1)
        if len(ss) == 2:
            f = ss[1]
            b = ss[0]
            if not b and not f:
                return False
            if b and not b.isdigit():
                return False
            if f and not f.isdigit():
                return False
            return True
        s = ss[0]
        return s.isdigit()
