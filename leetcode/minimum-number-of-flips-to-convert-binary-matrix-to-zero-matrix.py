#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        nm = n * m

        def flip(q, k):
            if q & (1 << k):
                q &= (~ (1 << k))
            else:
                q |= (1 << k)
            return q

        def next(q):
            res = []
            for k in range(nm):
                q2 = flip(q, k)
                i, j = k // m, k % m
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m:
                        q2 = flip(q2, x * m + y)
                res.append(q2)
            # print(q, res)
            return res

        visited = [0] * (1 << nm)
        q = 0
        for i in range(n):
            for j in range(m):
                k = i * m + j
                if mat[i][j]:
                    q = q | (1 << k)
        from collections import deque
        dq = deque()
        visited[q] = 1
        dq.append(q)

        while dq:
            q = dq.popleft()
            if q == 0:
                break
            d = visited[q]
            res = next(q)
            for q2 in res:
                if visited[q2] == 0:
                    visited[q2] = d + 1
                    dq.append(q2)

        ans = visited[0] - 1
        return ans
