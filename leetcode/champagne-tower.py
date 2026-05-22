#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """

        def split(v):
            if v >= 1:
                return (v - 1) * 0.5
            else:
                return 0

        glass = [[0] * (query_row + 1) for _ in range(2)]
        now = 0
        glass[now][0] = poured
        for i in range(1, query_row + 1):
            stop = True
            for j in range(i + 1):
                a = split(glass[now][j - 1]) if j > 0 else 0
                b = split(glass[now][j]) if j < i else 0
                v = a + b
                glass[1 - now][j] = v
                if v != 0:
                    stop = False
            if stop:
                return 0.0
            now = 1 - now
        return min(1, glass[now][query_glass])
