#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[i - 1].append(i)

        def bfs(root):
            d = [-1] * n
            q = deque()
            q.append((root, 0))
            while q:
                x, t = q.popleft()
                if d[x] != -1: continue
                d[x] = t
                if x == (n - 1): break
                for y in adj[x]:
                    if d[y] != -1: continue
                    q.append((y, t + 1))
            return d[-1]

        ans = []
        for x, y in queries:
            adj[x].append(y)
            r = bfs(0)
            ans.append(r)
        return ans


if __name__ == '__main__':
    pass
