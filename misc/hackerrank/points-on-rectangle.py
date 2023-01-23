#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.hackerrank.com/contests/101hack42/challenges/points-on-rectangle

def solve(pts):
    xs = [x[0] for x in pts]
    x_min = min(xs)
    x_max = max(xs)
    ys = [x[1] for x in pts]
    y_min = min(ys)
    y_max = max(ys)
    for p in pts:
        if x_min < p[0] < x_max and y_min < p[1] < y_max:
            return 'NO'
    return 'YES'


t = int(input())
for _ in range(t):
    q = int(input())
    pts = []
    for _ in range(q):
        pts.append([int(x) for x in input().rstrip().split()])
    print((solve(pts)))
