#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import math


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


# compute distance between two gps points.
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # km

    def to_radians(degree):
        return degree * math.pi / 180

    lat_delta = to_radians(lat2 - lat1)
    lon_delta = to_radians(lon2 - lon1)

    lat1 = to_radians(lat1)
    lat2 = to_radians(lat2)

    a = math.sin(lat_delta / 2) * math.sin(lat_delta / 2) + \
        math.cos(lat1) * math.cos(lat2) * math.sin(lon_delta / 2) * math.sin(lon_delta / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c  # in km
    return d


if __name__ == '__main__':
    print((haversine_distance(22.520525, 113.93145, 22.530525, 113.94145)))
