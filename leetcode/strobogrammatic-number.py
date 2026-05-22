#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # write your code here

        n = len(num)
        s, e = 0, n - 1
        exps = ('00', '11', '69', '88', '96')
        while s <= e:
            x, y = num[s], num[e]
            ok = False
            for exp in exps:
                if x == exp[0] and y == exp[1]:
                    s += 1
                    e -= 1
                    ok = True
                    break
            if not ok:
                return False
        return True
