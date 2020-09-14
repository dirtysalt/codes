#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[0] * m for _ in range(n)]

        def _sort(i, j):
            x, y = i, j

            ps = []
            while x < n and y < m:
                ps.append(mat[x][y])
                x += 1
                y += 1
            ps.sort()

            x, y = i, j
            for p in ps:
                ans[x][y] = p
                x += 1
                y += 1

        for i in reversed(range(n)):
            _sort(i, 0)
        for i in range(1, m):
            _sort(0, i)
        return ans
