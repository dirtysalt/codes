#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])

        def corners():
            for i in range(n):
                yield i, 0
            for j in range(1, m):
                yield n - 1, j

        d = 0
        dx, dy = -1, 1
        ans = []
        for x, y in corners():
            tmp = []
            while 0 <= x < n and 0 <= y < m:
                tmp.append(matrix[x][y])
                x += dx
                y += dy

            if d == 1:
                tmp = tmp[::-1]
            ans.extend(tmp)
            d = 1 - d
        return ans
