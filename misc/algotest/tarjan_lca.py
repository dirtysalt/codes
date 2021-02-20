#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys
from collections import defaultdict


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


def tarjan_lca(graph, root, queries):
    query_index = defaultdict(list)
    ans = [-1] * len(queries)
    for idx, (u, v) in enumerate(queries):
        query_index[u].append((v, idx))
        query_index[v].append((u, idx))

    n = len(graph)
    ufs = UnionFindSet(n)
    visited = [0] * n

    def dfs(root):
        visited[root] = 1

        # answer queries.
        query = query_index[root]
        for v, idx in query:
            if not visited[v]:
                continue
            # 如果有对应的查询节点v, 并且这个节点之前访问过
            # 那么使用这个节点的parent.
            # 如果v是root的祖先节点的话，那么就是v
            # 如果v在另外一个树上的话，那么就是最早交汇的节点
            p = ufs.find(v)
            ans[idx] = p

        # continue to dfs.
        for v in graph[root]:
            if not visited[v]:
                dfs(v)
                # 遍历子节点之后，将子节点的父节点设置为自己
                ufs.set(v, root)

    dfs(root)
    return ans


def luogu_p3379():
    # 只能通过70%的测试数据，其他都是TLE.
    # https://www.luogu.org/problemnew/show/P3379
    # sys.stdin = open('input.in')
    rl = sys.stdin.readline
    n, m, root = [int(x) for x in rl().split()]
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = [int(x) for x in rl().split()]
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    queries = []
    for _ in range(m):
        u, v = [int(x) for x in rl().split()]
        queries.append((u - 1, v - 1))

    root = root - 1
    ans = tarjan_lca(graph, root, queries)
    for x in ans:
        print(x + 1)


if __name__ == '__main__':
    luogu_p3379()
