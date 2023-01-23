#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, e, xs):
    edges = []
    for i in range(n):
        edges.append([])
    for i in range(e):
        a = xs[3 * i] - 1
        b = xs[3 * i + 1] - 1
        c = xs[3 * i + 2]
        edges[a].append((b, c))
        edges[b].append((a, c))
    return kruskal_solve(edges, n)


# prim algorithm.
def prime_solve(edges, n):
    inf = 1 << 31
    dist = [(inf, -1, -1)] * n
    cut_nodes = set(range(n))
    mst_edges = []
    # (edge value, start node, end node)
    dist[0] = (0, -1, -1)
    while cut_nodes:
        min_dist = inf
        min_node = None
        for v in cut_nodes:
            if dist[v][0] < min_dist:
                min_dist = dist[v][0]
                min_node = v
        if min_node is None:
            break
        assert min_node is not None
        cut_nodes.remove(min_node)
        mst_edges.append(dist[min_node])

        for v, val in edges[min_node]:
            if v not in cut_nodes:
                continue
            if val < dist[v][0]:
                dist[v] = (val, min_node, v)
    # print(mst_edges)
    res = sum([x[0] for x in mst_edges])
    return res


# kruskal algorithm.
def kruskal_solve(edges, n):
    parent = [-1] * n
    es = []
    for v in range(n):
        for v2, d in edges[v]:
            if v >= v2:
                continue
            es.append((d, v, v2))
    es.sort(key=lambda x: x[0])

    def find_parent(x):
        while parent[x] != -1:
            x = parent[x]
        return x

    def merge_parent(u, v):
        # print('merge parent ({}, {})'.format(u, v))
        p = find_parent(u)
        # print('parent of {} = {}'.format(u, p))
        # compress u.
        u2 = u
        while u2 != p:
            tmp = parent[u2]
            parent[u2] = p
            u2 = tmp

        # compress v.
        v2 = v
        while v2 != -1:
            tmp = parent[v2]
            parent[v2] = p
            v2 = tmp

    mst_edges = []
    for (d, u, v) in es:
        if find_parent(u) == find_parent(v):
            continue
        # print(d, u, v)
        merge_parent(u, v)
        mst_edges.append((d, u, v))
    res = sum([x[0] for x in mst_edges])
    return res


def spanningTree(graph, n, e):
    edges = []
    for i in range(n):
        nxts = []
        for j in range(n):
            if graph[i][j]:
                nxts.append((j, graph[i][j]))
        edges.append(nxts)
    return kruskal_solve(edges, n)


t = int(input())
for _ in range(t):
    n, e = [int(x) for x in input().rstrip().split()]
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(n, e, xs))
