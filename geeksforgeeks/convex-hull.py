#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import functools


@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{} {}'.format(self.x, self.y)

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x > other.x:
            return False
        return self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# https://www.geeksforgeeks.org/orientation-3-ordered-points/
def orientation(p, q, r):
    s1y = q.y - p.y
    s1x = q.x - p.x
    s2y = r.y - q.y
    s2x = r.x - q.x
    # s1y / s1x vs. s2y / s2x
    # < means counter clockwise 0
    # = means colinear = 1
    # > means clockwise  = 2
    val = s1y * s2x - s2y * s1x
    if val == 0:
        return 1
    elif val < 0:
        return 0
    else:
        return 2


def solve(ps):
    # dedup points.
    ps.sort()
    tmp = []
    p = ps[0]
    for i in range(1, len(ps)):
        if ps[i] == p:
            continue
        tmp.append(p)
        p = ps[i]
    tmp.append(p)
    ps = tmp

    # find convex hull
    n = len(ps)
    if n < 3:
        return -1
    # right bottom-left points.
    l = 0
    for i in range(1, n):
        if (ps[i].x < ps[l].x) or (ps[i].x == ps[l].x and ps[i].y < ps[l].y):
            l = i
    res = []
    p = l
    while True:
        res.append(p)
        q = (p + 1) % n
        for i in range(n):
            if orientation(ps[p], ps[q], ps[i]) == 2:
                q = i
        if q == l:
            break
        p = q
    assert len(res) >= 3
    res = [ps[x] for x in res]
    res.sort()
    return ', '.join([str(x) for x in res])


t = int(input())
for _ in range(t):
    n = int(input())
    vs2 = []
    while len(vs2) != 2 * n:
        vs = [int(x) for x in input().strip().split()]
        vs2.extend(vs)
    ps = [Point(vs2[2 * i], vs2[2 * i + 1]) for i in range(n)]
    print(solve(ps))
