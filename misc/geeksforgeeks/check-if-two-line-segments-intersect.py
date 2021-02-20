#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# https://www.geeksforgeeks.org/orientation-3-ordered-points/
def orientation(p, q, r):
    s1y = q.y - p.y
    s1x = q.x - p.x
    s2y = r.y - q.y
    s2x = r.x - q.x
    # s1y / s1x vs. s2y / s2x
    # < means clockwise
    # = means colinear
    # > means counter-clockwise
    val = s1y * s2x - s2y * s1x
    if val == 0:
        return 'cl'
    elif val < 0:
        return 'cw'
    else:
        return 'cc'


def onsegment(p, r, q):
    return min(p.x, q.x) <= r.x <= max(p.x, q.x) and \
           min(p.y, q.y) <= r.y <= max(p.y, q.y)


# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 'cl' and onsegment(p1, p2, q1):
        return True
    if o2 == 'cl' and onsegment(p1, q2, q1):
        return True
    if o3 == 'cl' and onsegment(p2, p1, q2):
        return True
    if o4 == 'cl' and onsegment(p2, q1, q2):
        return True
    return False


t = int(input())
for _ in range(t):
    vs = [int(x) for x in input().strip().split()]
    p1 = Point(vs[0], vs[1])
    q1 = Point(vs[2], vs[3])
    vs = [int(x) for x in input().strip().split()]
    p2 = Point(vs[0], vs[1])
    q2 = Point(vs[2], vs[3])
    print(int(intersect(p1, q1, p2, q2)))
