#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        s = 0
        res = 0
        while s < len(row):
            print((row, s))

            a = row[s]
            b = row[s + 1]
            if a > b:
                a, b = b, a
            # pairs.
            if (b - a) == 1 and a % 2 == 0:
                s += 2
                continue

            # find one to swap.
            if a % 2 == 0:
                exp = a + 1
            else:
                exp = a - 1

            tmp = row[s + 2:].index(exp)
            tmp += s + 2
            row[s + 1], row[tmp] = row[tmp], row[s + 1]
            s += 2
            res += 1
        return res
