#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        pw = 1
        pc = 0
        while ((pw * 10) <= n):
            pw *= 10
            pc += 1

        while (n):
            x = n // pw
            y = n % pw
            if (x >= 1):
                if (x == 1):
                    res += (y + 1)
                else:
                    res += pw
            res += x * pc * (pw // 10)
            n = y
            # print('pc = {}, pw = {}, res = {}, n = {}'.format(pc, pw, res, n))
            pc -= 1
            pw = pw // 10
        return res
