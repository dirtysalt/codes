#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        s = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s[i][j] = s[i - 1][j]
            v = 0
            for j in range(1, m + 1):
                v += mat[i - 1][j - 1]
                s[i][j] += v

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r0 = max(i - K, 0)
                c0 = max(j - K, 0)
                r1 = min(i + K, n - 1)
                c1 = min(j + K, m - 1)

                a = s[r1 + 1][c1 + 1]
                b = s[r1 + 1][c0]
                c = s[r0][c1 + 1]
                d = s[r0][c0]
                v = a + d - b - c
                ans[i][j] = v
        return ans
