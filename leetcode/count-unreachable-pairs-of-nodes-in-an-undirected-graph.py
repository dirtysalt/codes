#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        conn = []
        visited = [0] * n

        def bfs(x):
            from collections import deque
            dq = deque()
            mask = set()
            dq.append(x)
            mask.add(x)
            while dq:
                x = dq.popleft()
                for y in adj[x]:
                    if y in mask: continue
                    mask.add(y)
                    dq.append(y)
            for y in mask:
                visited[y] = 1
            return len(mask)

        ans = 0
        for i in range(n):
            if visited[i] == 0:
                size = bfs(i)
                # lose connection to (n-size)
                ans += size * (n - size)

        return ans // 2


if __name__ == '__main__':
    pass
