#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        visit = [0] * n
        ans = [0] * n

        def dfs(x):
            from collections import Counter
            cnt = Counter()

            if visit[x]:
                return cnt

            visit[x] = 1
            for y in adj[x]:
                tmp = dfs(y)
                cnt.update(tmp)
            lbl = labels[x]
            cnt[lbl] += 1

            value = cnt[lbl]
            ans[x] = value
            return cnt

        dfs(0)
        return ans
