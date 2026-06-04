#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Tree:
    def __init__(self, s, e, maxsize):
        self.s = s
        self.e = e
        self.maxsize = maxsize
        self.left = self.right = None

    def __str__(self):
        return 'Tree(%s,%s,%s)' % (self.s, self.e, self.maxsize)


def printT(t, indent=0):
    if t is None:
        return
    ot = '  ' * indent + ' + '
    ot += str(t)
    print(ot)
    printT(t.left, indent + 1)
    printT(t.right, indent + 1)


def queryMax(t, s, e):
    if t is None or e < t.s or s > t.e or s > e:
        return 0

    s = max(t.s, s)
    e = min(t.e, e)
    if s == t.s and e == t.e:
        return t.maxsize

    a = queryMax(t.left, s, e)
    b = queryMax(t.right, s, e)
    return max(a, b)


def searchLeft(t, e, minsize):
    a, b = 0, e
    while a <= b:
        m = (a + b) // 2
        sz = queryMax(t, m, e)
        if sz >= minsize:
            a = m + 1
        else:
            b = m - 1
    # b is valid.
    return b


def searchRight(t, s, n, minsize):
    a, b = s, n - 1
    while a <= b:
        m = (a + b) // 2
        sz = queryMax(t, s, m)
        if sz >= minsize:
            b = m - 1
        else:
            a = m + 1
    # a is valid.
    return a


def handleQ(t, q, minsize, rooms, maxsize):
    if maxsize < minsize:
        return -1

    s, e = 0, len(rooms) - 1
    while s <= e:
        m = (s + e) // 2
        if rooms[m][0] >= q:
            e = m - 1
        else:
            s = m + 1

    # s is valid.
    # rooms[s][0] >= q
    if s == len(rooms):
        s = s - 1

    start = []
    if rooms[s][0] == q:
        start = [s, s]
    else:
        start = [s - 1, s]

    rids = []
    l = searchLeft(t, start[0], minsize)
    if l >= 0:
        rids.append(rooms[l][0])
    r = searchRight(t, start[1], len(rooms), minsize)
    if r < len(rooms):
        rids.append(rooms[r][0])

    dist = 1 << 30
    ans = -1
    for rid in rids:
        d = abs(rid - q)
        if d < dist:
            dist = d
            ans = rid
    return ans


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms = [tuple(x) for x in rooms]
        rooms.sort()
        # print(rooms)
        dq = []
        maxsize = 0
        for i in range(len(rooms)):
            size = rooms[i][1]
            maxsize = max(maxsize, size)
            dq.append(Tree(i, i, size))

        while len(dq) != 1:
            dq2 = []
            for i in range(0, len(dq) // 2 * 2, 2):
                a = dq[i]
                b = dq[i + 1]
                c = Tree(a.s, b.e, max(a.maxsize, b.maxsize))
                c.left = a
                c.right = b
                dq2.append(c)
            if len(dq) % 2 != 0:
                dq2.append(dq[-1])
            dq = dq2

        root = dq[0]
        # printT(root)

        ans = []
        for q, minsize in queries:
            res = handleQ(root, q, minsize, rooms, maxsize)
            ans.append(res)
        return ans


class Solution2:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        events = []

        for i in range(len(rooms)):
            rid, size = rooms[i]
            events.append((size, 0, rid, i))
        for i in range(len(queries)):
            rid, size = queries[i]
            events.append((size, 1, rid, i))

        events.sort(key=lambda x: (-x[0], x[1], x[2], x[3]))
        print(events)

        ans = [-1] * len(queries)

        from sortedcontainers import SortedList
        sl = SortedList()

        for ev in events:
            (size, type, rid, idx) = ev
            if type == 0:
                sl.add(rid)
            else:
                i = sl.bisect_left(rid)
                dist = 1 << 30
                res = -1
                for j in (i - 1, i, i + 1):
                    if 0 <= j < len(sl):
                        d = abs(sl[j] - rid)
                        if d < dist:
                            res = sl[j]
                            dist = d
                ans[idx] = res
        return ans


cases = [
    ([[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]], [3, -1, 3]),
    ([[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], [[2, 3], [2, 4], [2, 5]], [2, 1, 3]),
    ([[11, 6], [6, 11], [1, 22], [20, 2], [21, 7], [8, 15], [4, 17], [13, 22], [17, 16], [22, 11]],
     [[21, 20], [23, 24], [6, 20], [5, 23], [8, 1], [1, 4], [10, 11], [24, 10], [7, 12], [7, 7]],
     [13, -1, 1, -1, 8, 1, 8, 22, 8, 6])
    # ([[11, 6], [6, 11], [1, 22], [20, 2], [21, 7], [8, 15], [4, 17], [13, 22], [17, 16], [22, 11]],
    #  [[7, 7]],
    #  [6])
]

import aatest_helper

# for f in ('input3.txt',):
#     import os
#
#     if not os.path.exists(f): continue
#     with open(f) as fh:
#         a = eval(fh.readline())
#         b = eval(fh.readline())
#         cases.append((a, b, aatest_helper.ANYTHING))

aatest_helper.run_test_cases(Solution2().closestRoom, cases)

if __name__ == '__main__':
    pass
