#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * (n - 1)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x - 1].append(y - 1)
            adj[y - 1].append(x - 1)

        def maxDist(cs):
            def bfs(x):
                from collections import deque
                dq = deque()
                dq.append((x, 0))
                visited = set()
                visited.add(x)
                ret = 0
                while dq:
                    (x, d) = dq.pop()
                    ret = max(d, ret)
                    for y in adj[x]:
                        if y in cs and y not in visited:
                            visited.add(y)
                            dq.append((y, d + 1))
                if len(visited) != len(cs):
                    return 0
                return ret

            ret = 0
            for x in cs:
                d = bfs(x)
                if d == 0: return 0
                ret = max(ret, d)
            return ret

        for st in range(1, 1 << n):
            cs = set()
            for j in range(n):
                if (st >> j) & 0x1:
                    cs.add(j)
            if len(cs) < 2:
                continue
            v = maxDist(cs)
            # print(v)
            if v >= 1:
                ans[v - 1] += 1
        return ans


cases = [
    (4, [[1, 2], [2, 3], [2, 4]], [3, 4, 0]),
    (2, [[1, 2]], [1]),
    (3, [[1, 2], [2, 3]], [2, 1]),
    (7, [[1, 4], [1, 3], [2, 5], [2, 6], [3, 6], [6, 7]], [6, 7, 7, 5, 2, 0]),
    (8, [[1, 5], [2, 3], [2, 5], [2, 8], [4, 7], [6, 7], [6, 8]], [7, 8, 8, 6, 5, 2, 0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSubgraphsForEachDiameter, cases)
