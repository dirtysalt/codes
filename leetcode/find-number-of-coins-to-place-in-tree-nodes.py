#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        coins = [0] * n

        def dfs(x, p):
            A = []
            B = []
            if cost[x] >= 0:
                A.append(cost[x])
            else:
                B.append(cost[x])

            if len(adj[x]) == 1 and adj[x][0] == p:
                coins[x] = 1
                return A, B

            for y in adj[x]:
                if y == p: continue
                a, b = dfs(y, x)
                A.extend(a)
                B.extend(b)

            A.sort()
            B.sort()
            value = 0
            if len(A) >= 3:
                r = A[-1] * A[-2] * A[-3]
                value = max(r, value)
            if len(A) >= 1 and len(B) >= 2:
                r = B[0] * B[1] * A[-1]
                value = max(r, value)

            if len(A) + len(B) < 3:
                value = 1
            coins[x] = value

            return A[-3:], B[:3]

        a, b = dfs(0, -1)
        # print(a, b)
        return coins


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], cost=[1, 2, 3, 4, 5, 6],
                              res=[120, 1, 1, 1, 1, 1]),
    aatest_helper.OrderedDict(edges=[[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]],
                              cost=[1, 4, 2, 3, 5, 7, 8, -4, 2], res=[280, 140, 32, 1, 1, 1, 1, 1, 1]),
    aatest_helper.OrderedDict(edges=[[0, 1], [0, 2]], cost=[1, 2, -2], res=[0, 1, 1]),
    ([[0, 1]], [1, 2], [1, 1]),
]

aatest_helper.run_test_cases(Solution().placedCoins, cases)

if __name__ == '__main__':
    pass
