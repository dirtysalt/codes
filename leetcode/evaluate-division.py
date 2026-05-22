#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        index = {}
        for x, y in equations:
            if x not in index:
                index[x] = len(index)
            if y not in index:
                index[y] = len(index)

        n = len(index)
        graph = [[] for _ in range(n)]
        for (x, y), v in zip(equations, values):
            ix = index[x]
            iy = index[y]
            graph[ix].append((iy, v))
            graph[iy].append((ix, 1 / v))

        def bfs(s, e):
            from collections import deque
            dq = deque()
            visited = [0] * n
            dq.append((s, 1.0))
            visited[s] = 1

            while dq:
                (s, v) = dq.popleft()
                if s == e:
                    return v

                for x, r in graph[s]:
                    if visited[x]:
                        continue
                    visited[x]
                    dq.append((x, v * r))

            return -1.0

        ans = []
        for (s, e) in queries:
            if s not in index or e not in index:
                ans.append(-1.0)
                continue
            s = index[s]
            e = index[e]
            res = bfs(s, e)
            ans.append(round(res, 5))

        return ans


cases = [
    ([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
     [6.0, 0.5, -1.0, 1.0, -1.0]),
    ([["a", "e"], ["b", "e"]], [4.0, 3.0], [["a", "b"], ["e", "e"], ["x", "x"]], [1.33333, 1.0, -1.0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().calcEquation, cases)
