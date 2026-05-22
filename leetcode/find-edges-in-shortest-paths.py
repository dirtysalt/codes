#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        def shortest(u):
            import heapq
            pq = []
            dist = [-1] * n
            pq.append((0, u))
            while pq:
                d, x = heapq.heappop(pq)
                if dist[x] != -1: continue
                dist[x] = d
                for y, w in adj[x]:
                    if dist[y] != -1: continue
                    heapq.heappush(pq, (d + w, y))
            return dist

        A = shortest(0)
        B = shortest(n - 1)
        D = A[n - 1]
        assert (A[n - 1] == B[0])

        ans = []
        for u, v, w in edges:
            ok = False
            if D != -1 and A[u] != -1 and B[v] != -1:
                if (A[u] + B[v] + w) == D or (A[v] + B[u] + w) == D:
                    ok = True
            ans.append(ok)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=6, edges=[[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3],
                                          [4, 5, 2]], res=[true, true, true, false, true, true, true, false]),
    aatest_helper.OrderedDict(n=4, edges=[[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]], res=[true, false, false, true]),
]

aatest_helper.run_test_cases(Solution().findAnswer, cases)

if __name__ == '__main__':
    pass
