#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq
import os
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:

        # build adj on fixed cost
        # assign varied cost with 1.
        adj = [[] for _ in range(n)]
        disconnect = set()
        for a, b, w in edges:
            if w == -1:
                disconnect.add((a, b))
                disconnect.add((b, a))
                w = 1
            adj[a].append((b, w))
            adj[b].append((a, w))

        def shortest(s, e, adj):
            visit = [-1] * n
            import heapq
            hp = []
            hp.append((0, s, -1))
            while hp:
                (d, x, p) = heapq.heappop(hp)
                if visit[x] != -1: continue
                visit[x] = d
                if x == e: break
                for y, w in adj[x]:
                    if visit[y] != -1: continue
                    heapq.heappush(hp, (d + w, y, x))
            return visit

        if True:
            D1 = shortest(destination, source, adj)
            d = D1[source]
            if d > target:
                return []

        # dijkstra again with deterministic order.
        def fixedWeight(s, e, adj, D):
            visit = [-1] * n
            hp = []
            hp.append((0, s, -1, 0))
            weight = {}
            while hp:
                (d, x, p, w) = heapq.heappop(hp)
                if visit[x] != -1: continue
                visit[x] = d
                if p != -1:
                    weight[(x, p)] = w
                if x == e: break
                for y, w in adj[x]:
                    if (x, y) in disconnect:
                        if D[y] != -1 and (d + D[y] + w) <= target:
                            w = target - d - D[y]
                        else:
                            w = target + 1
                    if visit[y] != -1: continue
                    heapq.heappush(hp, (d + w, y, x, w))
            return visit, weight

        D2, W = fixedWeight(source, destination, adj, D1)
        if D2[destination] != target:
            return []

        output = []
        for a, b, w in edges:
            if w != -1:
                output.append((a, b, w))
                continue

            w = W.get((a, b)) or W.get((b, a)) or w
            if w == -1:
                w = target + 1
            output.append((a, b, w))
        output = [list(x) for x in output]

        DOCHECK = False
        if os.environ.get('USER') == 'dirlt':
            # print('mother')
            DOCHECK = True

        if DOCHECK:
            def check(edges):
                adj = [[] for _ in range(n)]
                for a, b, w in edges:
                    adj[a].append((b, w))
                    adj[b].append((a, w))
                D = shortest(source, destination, adj)
                if D[destination] != target:
                    print('FAILED', D[destination], target)

            check(output)

        return output


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 0, 1, 5, [[4, 1, 1], [2, 0, 1], [0, 3, 3], [4, 3, 1]]),
    (3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6, []),
    (4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, 1]]),
    (4, [[0, 1, -1], [1, 2, -1], [3, 1, -1], [3, 0, 2], [0, 2, 5]], 2, 3, 8, []),
    (4, [[0, 1, -1], [2, 0, 2], [3, 2, 6], [2, 1, 10], [3, 0, -1]], 1, 3, 12,
     [[0, 1, 11], [2, 0, 2], [3, 2, 6], [2, 1, 10], [3, 0, 1]]),
    (2, [[1, 0, -1]], 0, 1, 5, [[1, 0, 5]]),
    (5, [[1, 4, 1], [2, 4, -1], [3, 0, 2], [0, 4, -1], [1, 3, 10], [1, 0, 10]], 0, 2, 15,
     [[1, 4, 1], [2, 4, 4], [3, 0, 2], [0, 4, 14], [1, 3, 10], [1, 0, 10]]),
    (5, [[0, 3, 1], [1, 2, -1], [2, 3, 7], [4, 2, 1], [2, 0, -1], [4, 1, 9], [3, 4, 9]], 0, 1, 18,
     [[0, 3, 1], [1, 2, 10], [2, 3, 7], [4, 2, 1], [2, 0, 17], [4, 1, 9], [3, 4, 9]]),
    (
        5, [[1, 3, 10], [4, 2, -1], [0, 3, 7], [4, 0, 7], [3, 2, -1], [1, 4, 5], [2, 0, 8], [1, 0, 3], [1, 2, 5]], 3, 4,
        11,
        [[1, 3, 10], [4, 2, 1], [0, 3, 7], [4, 0, 7], [3, 2, 10], [1, 4, 5], [2, 0, 8], [1, 0, 3], [1, 2, 5]]),
]

aatest_helper.run_test_cases(Solution().modifiedGraphEdges, cases)

if __name__ == '__main__':
    pass
