#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin
n = int(fh.readline())
a = [int(x) - 1 for x in fh.readline().strip().split(' ')]

from queue import Queue

track_set = [0] * (4 ** 10)
Q = Queue()


def possible_moves(a):
    d = [-1] * 4
    for (x, p) in enumerate(a):
        if d[p] == -1:
            d[p] = x
    states = []
    for i in range(4):
        if d[i] == -1:
            continue
        for j in range(4):
            if d[j] == -1 or d[i] < d[j]:
                a2 = a[::]
                a2[d[i]] = j
                states.append(a2)
    # print states
    return states


def hx(a):
    v = 0
    for x in a[::-1]:
        v = v * 4 + x
    return v


def fx(h):
    a = []
    for i in range(n):
        a.append(h % 4)
        h /= 4
    return a


# h = hx([0,3,1])
# print fx(h)

h = hx(a)
Q.put((h, 0))
track_set[h] = 1
while True:
    (h, cnt) = Q.get()
    if h == 0:
        break
    a = fx(h)
    moves = possible_moves(a)
    for m in moves:
        h = hx(m)
        if track_set[h]:
            continue
        Q.put((h, cnt + 1))
        track_set[h] = 1

print(cnt)
