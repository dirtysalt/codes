#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import defaultdict
from typing import List


def tarjan_lca(graph, root, queries):
    class UnionFindSet:
        def __init__(self, n):
            self.ps = [0] * n
            for i in range(n):
                self.ps[i] = i

        def find(self, x):
            p = x
            while self.ps[p] != p:
                p = self.ps[p]

            while self.ps[x] != x:
                up = self.ps[x]
                self.ps[x] = p
                x = up
            return p

        def set(self, x, p):
            self.ps[x] = p

    query_index = defaultdict(list)
    ans = [-1] * len(queries)
    for idx, (u, v) in enumerate(queries):
        query_index[u].append((v, idx))
        query_index[v].append((u, idx))

    n = len(graph)
    ufs = UnionFindSet(n)

    def dfs(root, parent):
        # answer queries.
        query = query_index[root]
        for v, idx in query:
            # 如果有对应的查询节点v, 并且这个节点之前访问过
            # 那么使用这个节点的parent.
            # 如果v是root的祖先节点的话，那么就是v
            # 如果v在另外一个树上的话，那么就是最早交汇的节点
            p = ufs.find(v)
            if p != -1:
                ans[idx] = p

        # continue to dfs.
        for v, _ in graph[root]:
            if v != parent:
                dfs(v, root)
                # 遍历子节点之后，将子节点的父节点设置为自己
                ufs.set(v, root)

    dfs(root, -1)
    return ans


class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for (u, v, w) in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        W = {}

        def dfs(root, parent, weight):
            W[root] = tuple(weight)
            for v, w in adj[root]:
                if v == parent: continue
                weight[w] += 1
                dfs(v, root, weight)
                weight[w] -= 1

        dfs(0, -1, [0] * 27)
        lca = tarjan_lca(adj, 0, queries)
        ans = []
        for (u, v), r in zip(queries, lca):
            w1 = list(W[u])
            w2 = list(W[v])
            w3 = list(W[r])
            for i in range(27):
                w1[i] -= w3[i]
                w2[i] -= w3[i]
                w1[i] += w2[i]
            c = sum(w1) - max(w1)
            ans.append(c)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (7, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 2], [4, 5, 2], [5, 6, 2]], [[0, 3], [3, 6], [2, 6], [0, 6]],
     [0, 0, 1, 3]),
    (8, [[1, 2, 6], [1, 3, 4], [2, 4, 6], [2, 5, 3], [3, 6, 6], [3, 0, 8], [7, 0, 2]], [[4, 6], [0, 4], [6, 5], [7, 4]],
     [1, 2, 2, 3]),
]

aatest_helper.run_test_cases(Solution().minOperationsQueries, cases)

if __name__ == '__main__':
    pass
