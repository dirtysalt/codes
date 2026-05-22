#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(edges, n):
    dist = edges[::]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                p0 = i * n + j
                p1 = i * n + k
                p2 = k * n + j
                dist[p0] = min(dist[p0], dist[p1] + dist[p2])
    return ' '.join(map(str, dist))


t = int(input())
for _ in range(t):
    n = int(input())
    edges = [int(x) for x in input().rstrip().split()]
    print(solve(edges, n))
