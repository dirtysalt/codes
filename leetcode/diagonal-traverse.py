#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        i, j, d = 0, 0, 0

        ans = []
        for _ in range(n * m):
            ans.append(matrix[i][j])

            if d == 0:
                dx, dy = (-1, 1)
                x, y = i + dx, j + dy
                if x == -1 or y == m:
                    d = 1 - d

                    if x == -1 and y == m:
                        x, y = 1, m - 1
                    elif x == -1:
                        x = 0
                    else:
                        x += 2
                        y = m - 1


            else:
                dx, dy = (1, -1)
                x, y = i + dx, j + dy
                if x == n or y == -1:
                    d = 1 - d

                    if x == n and y == -1:
                        x, y = n - 1, 1
                    elif y == -1:
                        y = 0
                    else:
                        y += 2
                        x = n - 1
            i, j = x, y
        return ans
