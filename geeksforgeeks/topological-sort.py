#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n, graph):
    ins = [0] * n
    for i in range(n):
        vs = graph[i]
        for v in vs:
            ins[v] += 1
    res = []
    nodes = set(range(n))
    while nodes:
        ok = None
        for v in nodes:
            if ins[v] == 0:
                ok = v
                break
        res.append(ok)
        nodes.remove(ok)
        for v in graph[ok]:
            ins[v] -= 1
    return res


topoSort = solve

t = int(input())
for _ in range(t):
    n, e = [int(x) for x in input().rstrip().split()]
    ps = [int(x) for x in input().rstrip().split()]
    graph = []
    for _ in range(n):
        graph.append([])
    for i in range(e):
        a = ps[2 * i]
        b = ps[2 * i + 1]
        graph[a].append(b)
    print(solve(n, graph))
