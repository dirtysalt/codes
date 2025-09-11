#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(M)
        m = len(M[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                val = 0
                cnt = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < n and 0 <= j2 < m:
                            val += M[i2][j2]
                            cnt += 1
                ans[i][j] = val // cnt
        return ans
