#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0

        max_dist = []
        for i in range(n):
            max_dist.append([-1] * m)

        def dfs(r, c):
            if max_dist[r][c] != -1:
                return max_dist[r][c]
            val = matrix[r][c]
            ans = 0
            for (dr, dc) in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r2 = r + dr
                c2 = c + dc
                if r2 >= n or r2 < 0 or c2 >= m or c2 < 0 or matrix[r2][c2] <= val:
                    continue
                res = dfs(r2, c2)
                ans = max(ans, res)
            ans += 1
            max_dist[r][c] = ans
            return ans

        ans = 0
        for i in range(n):
            for j in range(m):
                res = dfs(i, j)
                ans = max(ans, res)
        return ans
