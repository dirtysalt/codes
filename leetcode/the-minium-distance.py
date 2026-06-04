#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.lintcode.com/problem/the-minium-distance/description

class Solution:
    """
    @param mazeMap: a 2D grid
    @return: return the minium distance
    """

    def getMinDistance(self, mazeMap):
        # write your code here
        n, m = len(mazeMap), len(mazeMap[0])
        from collections import defaultdict
        adj = defaultdict(list)
        start = None
        for i in range(n):
            for j in range(m):
                v = mazeMap[i][j]
                if v > 0:
                    adj[v].append(i * m + j)
                if v == -3:
                    start = i * m + j

        from collections import deque
        dq = deque()
        visited = [-1] * (n * m)
        dq.append(start)
        visited[start] = 0
        used = set()

        # print(start, end, adj)
        ans = -1
        while dq:
            k = dq.popleft()
            d = visited[k]
            i, j = k // m, k % m
            v = mazeMap[i][j]
            if v == -2:
                ans = d
                break

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + dx, j + dy
                kk = x * m + y
                if 0 <= x < n and 0 <= y < m and mazeMap[x][y] != -1 and visited[kk] == -1:
                    visited[kk] = d + 1
                    dq.append(kk)

            if v > 0 and v not in used:
                for kk in adj[v]:
                    if kk != k and visited[kk] == -1:
                        visited[kk] = d + 1
                        dq.append(kk)
                used.add(v)
        return ans
