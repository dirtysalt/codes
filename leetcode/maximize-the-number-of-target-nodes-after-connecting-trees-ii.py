#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def edge2adj(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def build_dist(adj):
            n = len(adj)
            record = [[0, 0] for _ in range(n)]

            def dfs(x, p):
                record[x][0] += 1
                if len(adj[x]) == 1 and adj[x][0] == p:
                    return

                for y in adj[x]:
                    if y == p: continue
                    dfs(y, x)
                    record[x][0] += record[y][1]
                    record[x][1] += record[y][0]

            def backprop(x, p):
                if p != -1:
                    ra, rb = record[p]
                    a, b = record[x]
                    ra -= b
                    rb -= a
                    record[x][0] += rb
                    record[x][1] += ra

                for y in adj[x]:
                    if y == p: continue
                    backprop(y, x)

            dfs(0, -1)
            # print('dfs...')
            # print(record)
            backprop(0, -1)
            # print('backprop...')
            # print(record)
            return record

        adj1 = edge2adj(edges1)
        adj2 = edge2adj(edges2)
        dist1 = build_dist(adj1)
        dist2 = build_dist(adj2)
        base = max(r[1] for r in dist2)
        # print(dist1, base)

        n = len(edges1) + 1
        ans = []
        for i in range(n):
            ans.append(dist1[i][0] + base)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
                              edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]],
                              res=[8, 7, 7, 8, 8]),
    aatest_helper.OrderedDict(edges1=[[0, 1], [0, 2], [0, 3], [0, 4]], edges2=[[0, 1], [1, 2], [2, 3]],
                              res=[3, 6, 6, 6, 6])
]

aatest_helper.run_test_cases(Solution().maxTargetNodes, cases)

if __name__ == '__main__':
    pass
