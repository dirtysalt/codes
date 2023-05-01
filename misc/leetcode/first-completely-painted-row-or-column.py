#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [0] * n
        cols = [0] * m

        pos = {}
        for i in range(n):
            for j in range(m):
                pos[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            (x, y) = pos[arr[i]]
            rows[x] += 1
            cols[y] += 1
            if rows[x] == m or cols[y] == n:
                return i
        return -1


if __name__ == '__main__':
    pass
