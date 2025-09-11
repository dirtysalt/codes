#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def Kruskal(ei, contain):
            fa = [-1] * n

            def father(a):
                p = a
                while fa[p] != -1:
                    p = fa[p]

                while a != p:
                    x = fa[a]
                    fa[a] = p
                    a = x

                return p

            def union(a, b):
                fa[a] = b

            es = []
            ans = 0

            if ei != -1 and contain:
                f, t, w = edges[ei]
                union(f, t)
                ans += w

            for i in range(len(edges)):
                if i != ei:
                    f, t, w = edges[i]
                    es.append((w, f, t, i))

            es.sort()
            for e in es:
                w, f, t, idx = e
                ff = father(f)
                ft = father(t)
                if ff == ft:
                    continue
                union(ff, ft)
                ans += w
            return ans

        weight = Kruskal(-1, contain=False)
        keys = []
        nkeys = []
        for i in range(len(edges)):
            w = Kruskal(i, contain=False)
            if w != weight:
                # if remove i from candidate edges, we don't have same weight, it must be key edge.
                keys.append(i)
                continue

            w = Kruskal(i, contain=True)
            if w == weight:
                # if keep i in candidate edges, and we have same weight, it must be non-key edge.
                nkeys.append(i)
                continue

        ans = [keys, nkeys]
        return ans


import aatest_helper

cases = [
    (5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]], [[0, 1], [2, 3, 4, 5]]),
    (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], [[], [0, 1, 2, 3]])
]
aatest_helper.run_test_cases(Solution().findCriticalAndPseudoCriticalEdges, cases)
