#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = {}
        cols = {}
        for i in range(n):
            acc = 0
            for j in range(m):
                acc += mat[i][j]
            rows[i] = acc

        for i in range(m):
            acc = 0
            for j in range(n):
                acc += mat[j][i]
            cols[i] = acc

        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    a = rows[i]
                    b = cols[j]
                    if a == 1 and b == 1:
                        ans += 1
        return ans
