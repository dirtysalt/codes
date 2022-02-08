#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import deque

from typing import List

import aatest_helper


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        my_routes = [set(x) for x in routes]
        n = len(my_routes)

        def has_connection(i, j):
            return bool(my_routes[i] & my_routes[j])

        if S == T: return 0

        # # build graph in matrix. O(n^2)
        # graph = []
        # for i in range(n):
        #     graph.append([-1] * n)
        #
        # for i in range(n):
        #     graph[i][i] = 0
        #     for j in range(i + 1, n):
        #         conn = has_connection(i, j)
        #         graph[i][j] = graph[j][i] = 1 if conn else -1
        #
        # # floyd-warshall. O(n^3)
        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if graph[i][k] != -1 and graph[k][j] != -1:
        #                 val = graph[i][k] + graph[k][j]
        #                 if graph[i][j] == -1:
        #                     graph[i][j] = val
        #                 else:
        #                     graph[i][j] = min(graph[i][j], val)

        # build graph in adjacent list. O(n^2)
        graph = []
        for i in range(n):
            graph.append([])

        for i in range(n):
            for j in range(i + 1, n):
                conn = has_connection(i, j)
                if conn:
                    graph[i].append(j)
                    graph[j].append(i)

        # BFS. O(n)
        def shortest_path(s, t):
            dq = deque()
            dist = [-1] * n
            dist[s] = 0
            dq.append(s)
            while len(dq):
                x = dq.popleft()
                if x == t:
                    return dist[x]
                for y in graph[x]:
                    if dist[y] == -1:
                        dist[y] = dist[x] + 1
                        dq.append(y)
            return -1

        src_idxs = set([i for i in range(n) if S in my_routes[i]])
        dst_idxs = set([i for i in range(n) if T in my_routes[i]])

        # 如果存在交集的话，那么不用任何换乘
        if src_idxs & dst_idxs:
            return 1
        sts = [(i, j) for i in src_idxs for j in dst_idxs]
        res = (n + 1)
        for s, t in sts:
            val = shortest_path(s, t)
            if val != -1:
                res = min(res, val)
        if res == (n + 1):
            return -1
        return res + 1


cases = [
    ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
    ([[1, 2, 3], [3, 4, 5], [4, 5, 6]], 1, 6, 3),
    ([[1, 2, 3], [3, 4, 5], [4, 5, 6], [2, 3, 6]], 1, 6, 2),
    ([[1, 2, 3]], 1, 4, -1),
    ([[1, 7], [3, 5]], 5, 5, 0),
    # aatest_helper.read_case_from_file('/Users/dirlt/playbook/input.in', 1),
]

sol = Solution()

aatest_helper.run_test_cases(sol.numBusesToDestination, cases)
