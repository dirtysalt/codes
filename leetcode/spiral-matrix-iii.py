#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        visited = 0
        RC = R * C
        direction = 0
        step = 0
        r, c = r0, c0
        res = []

        res.append((r0, c0))
        visited += 1
        while visited < RC:
            if direction == 0 or direction == 2:
                step += 1

            if direction == 0:
                delta = (0, 1)
            elif direction == 1:
                delta = (1, 0)
            elif direction == 2:
                delta = (0, -1)
            else:
                delta = (-1, 0)

            for _ in range(step):
                r2 = r + delta[0]
                c2 = c + delta[1]
                if 0 <= r2 < R and 0 <= c2 < C:
                    visited += 1
                    res.append((r2, c2))
                r = r2
                c = c2
            direction = (direction + 1) % 4

        return res
