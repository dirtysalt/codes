#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s, e = 1, num
        while s <= e:
            m = (s + e) // 2
            m2 = m * m
            if m2 > num:
                e = m - 1
            elif m2 < num:
                s = m + 1
            else:
                return True
        return False
