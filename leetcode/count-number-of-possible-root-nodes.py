#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        ss = {(x, y) for (x, y) in guesses}

        def dfs(x, p):
            r = 0
            for y in adj[x]:
                if y == p: continue
                r += ((x, y) in ss)
                r += dfs(y, x)
            return r

        base = dfs(0, -1)

        def reroot(x, p, now):
            r = 0
            if now >= k: r += 1
            for y in adj[x]:
                if y == p: continue
                r += reroot(y, x, (now - ((x, y) in ss) + ((y, x) in ss)))
            return r

        ans = reroot(0, -1, base)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 1], [1, 2], [1, 3], [4, 2]], [[1, 3], [0, 1], [1, 0], [2, 4]], 3, 3),
    ([[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 0], [3, 4], [2, 1], [3, 2]], 1, 5),
]

aatest_helper.run_test_cases(Solution().rootCount, cases)

if __name__ == '__main__':
    pass
