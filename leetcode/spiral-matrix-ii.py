#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        mat = [[0 for _ in range(n)] for _ in range(n)]
        d, r, c = 0, 0, -1
        value = 0
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        last_d = -1

        while True:
            dr, dc = delta[d]
            while True:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < n and 0 <= c2 < n and not mat[r2][c2]:
                    value += 1
                    r, c = r2, c2
                    mat[r][c] = value
                    last_d = d
                else:
                    break
            d = (d + 1) % 4
            if d == last_d:
                break
        return mat
