#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 这道题目很有意思，可以从海岸线上面的点反向探索。
# 在递归阶段，如果结果需要到最后一层才能知道的话，那么在递归阶段必须确保没有回路
# 更好的办法是一开始就知道结果，然后反向推导。

class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(matrix)
        if not n: return []
        m = len(matrix[0])
        if not m: return []

        def dfs(r, c, ocean):
            ocean.add((r, c))
            for (dr, dc) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < n and 0 <= c2 < m and matrix[r][c] <= matrix[r2][c2] and (r2, c2) not in ocean:
                    dfs(r2, c2, ocean)

        pac = set()
        alt = set()
        for i in range(m):
            dfs(0, i, pac)
            dfs(n - 1, i, alt)
        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m - 1, alt)

        res = list(pac & alt)
        return res
