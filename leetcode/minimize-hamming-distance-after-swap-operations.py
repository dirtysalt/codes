#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        adj = [[] for _ in range(n)]

        for x, y in allowedSwaps:
            adj[x].append(y)
            adj[y].append(x)

        vis = [0] * n

        def dfs(x, c):
            vis[x] = c
            for x2 in adj[x]:
                if vis[x2]: continue
                vis[x2] = c
                dfs(x2, c)

        conn = 1
        for x in range(n):
            if vis[x]: continue
            dfs(x, conn)
            conn += 1

        from collections import Counter, defaultdict
        dist = defaultdict(list)
        for i in range(n):
            dist[vis[i]].append(i)

        ans = 0
        for idxs in dist.values():
            tc = Counter([target[i] for i in idxs])
            for i in idxs:
                x = source[i]
                if tc[x] == 0:
                    ans += 1
                else:
                    tc[x] -= 1
        return ans


cases = [
    ([1, 2, 3, 4], [2, 1, 4, 5], [[0, 1], [2, 3]], 1),
    ([1, 2, 3, 4], [1, 3, 2, 4], [], 2),
    ([5, 1, 2, 4, 3], [1, 5, 4, 2, 3], [[0, 4], [4, 2], [1, 3], [1, 4]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumHammingDistance, cases)
