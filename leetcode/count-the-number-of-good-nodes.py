#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        ans = [0]

        def dfs(r, p):
            if len(adj[r]) == 1 and adj[r][0] == p:
                ans[0] += 1
                return 1

            c = []
            for x in adj[r]:
                if x == p: continue
                h = dfs(x, r)
                c.append(h)

            if all((x == c[0] for x in c)):
                ans[0] += 1
            return sum(c) + 1

        dfs(0, -1)
        return ans[0]


if __name__ == '__main__':
    pass
