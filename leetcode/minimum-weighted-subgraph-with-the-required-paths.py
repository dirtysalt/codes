#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
#
#         INF = 1 << 63
#
#         adj = [[] for _ in range(n)]
#         for x, y, w in edges:
#             adj[x].append((y, w))
#
#         def find1():
#             vis = [0] * n
#             choose = set()
#
#             def dfs(x, cost):
#                 if x == dest:
#                     res = find2(choose)
#                     if res == INF:
#                         return INF
#                     return res + cost
#
#                 ans = INF
#                 for y, w in adj[x]:
#                     if vis[y]: continue
#                     vis[y] = 1
#                     choose.add((x, y))
#                     res = dfs(y, w + cost)
#                     ans = min(ans, res)
#                     choose.remove((x, y))
#                     vis[y] = 0
#                 return ans
#
#             vis[src1] = 1
#             ans = dfs(src1, 0)
#             vis[src1] = 0
#             return ans
#
#         def find2(choose):
#             # print(choose)
#             vis = [0] * n
#             import heapq
#             hp = []
#             heapq.heappush(hp, (0, src2))
#             while hp:
#                 (c, x) = heapq.heappop(hp)
#                 if x == dest:
#                     return c
#                 vis[x] = 1
#                 for y, w in adj[x]:
#                     if vis[y]: continue
#                     if (x, y) in choose:
#                         w = 0
#                     heapq.heappush(hp, (w + c, y))
#             return INF
#
#         ans = find1()
#         if ans == INF:
#             ans = -1
#         return ans

from typing import List

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        INF = 1 << 63

        adj = [[] for _ in range(n)]
        badj = [[] for _ in range(n)]
        for x, y, w in edges:
            adj[x].append((y, w))
            badj[y].append((x, w))

        def search(x, adj):
            dist = [-1] * n
            import heapq
            hp = [(0, x)]
            while hp:
                (c, x) = heapq.heappop(hp)
                if dist[x] != -1:
                    continue
                dist[x] = c
                for y, w in adj[x]:
                    if dist[y] != -1: continue
                    heapq.heappush(hp, (w + c, y))
            return dist

        D = search(dest, badj)
        A = search(src1, adj)
        B = search(src2, adj)
        # print(D, A, B)
        ans = INF
        for x in range(n):
            if D[x] == -1 or A[x] == -1 or B[x] == -1:
                continue
            d = D[x] + A[x] + B[x]
            ans = min(ans, d)

        if ans == INF:
            return -1
        return ans

true, false, null = True, False, None
cases = [
    (
        6, [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]], 0, 1, 5,
        9),
    (3, [[0, 1, 1], [2, 1, 1]], 0, 1, 2, -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumWeight, cases)

if __name__ == '__main__':
    pass
