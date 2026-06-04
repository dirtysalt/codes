#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n, pairs):
    edges = []
    for _ in range(n):
        edges.append([])
    for i in range(n - 1):
        v0 = pairs[2 * i] - 1
        v1 = pairs[2 * i + 1] - 1
        edges[v0].append(v1)
        edges[v1].append(v0)

    res = 0
    v = 0
    dist = [-1] * n
    dist[v] = 0
    queue = [v]
    while queue:
        v2 = queue[0]
        queue.pop(0)
        for v3 in edges[v2]:
            if dist[v3] != -1:
                continue
            dist[v3] = dist[v2] + 1
            queue.append(v3)
    # start with 0.
    # separate two sets
    a, b = 0, 0
    for v in range(n):
        assert dist[v] >= 0
        if dist[v] % 2 == 0:
            a += 1
        else:
            b += 1
    res += a * (a - 1) // 2
    res += b * (b - 1) // 2
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    pairs = [int(x) for x in input().rstrip().split()]
    print(solve(n, pairs))
