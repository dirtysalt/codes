#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

inf = 100000000


class Tree:
    def __init__(self, l, r, s, sz):
        self.data = (l, r, s, sz)
        self.left = self.right = None


def printT(t, ident=0):
    if t is None:
        return
    ot = '  ' * ident + '+ '
    (a, b, s, sz) = t.data
    if s == -1:
        ot += 'Lef: (%d, %d), sz: %d' % (a, b, sz)
    else:
        ot += 'Pat: (%d, %d), split: %d' % (a, b, s)

    print(ot)
    if t:
        printT(t.left, ident + 1)
        printT(t.right, ident + 1)


def merge(L, R):
    (ll, lr, _, lsz) = L.data
    (rl, rr, _, rsz) = R.data
    assert (lr == rl)
    t = Tree(ll, rr, lr, max(lsz, rsz))
    t.left = L
    t.right = R
    return t


def cons(data):
    assert (len(data) > 0)
    (a, b, sz) = data[0]
    root = Tree(a, b, -1, sz)

    for i in range(1, len(data)):
        (a, b, sz) = data[i]
        t = Tree(a, b, -1, sz)
        root = merge(root, t)
    return root


def mergeAndFilter(data):
    data = [(x, y, z) for (x, y, z) in data if x != y]
    out = []
    x, y, z = data[0]
    for i in range(1, len(data)):
        if data[i][2] == z:
            y = data[i][1]
        else:
            out.append((x, y, z))
            x, y, z = data[i]
    out.append((x, y, z))
    return out


def insert(t, a, b, sz):
    if t is None:
        return Tree(a, b, -1, sz)

    l, r, s, sz2 = t.data
    if b <= l or a >= r:
        return t

    if a >= l and b <= r and sz >= sz2:
        return t

    if s == -1:
        osz = min(sz2, sz)
        if a < l:
            if b < r:
                data = [(a, l, sz), (l, b, osz), (b, r, sz2)]
            else:
                data = [(a, l, sz), (l, r, osz), (r, b, sz)]
        else:
            if b < r:
                data = [(l, a, sz2), (a, b, osz), (b, r, sz2)]
            else:
                data = [(l, a, sz2), (a, r, osz), (r, b, sz)]
        data = mergeAndFilter(data)
        assert len(data) > 0
        return cons(data)

    # left is [l, s)
    # right is [s, r)
    if a < s:
        L = insert(t.left, a, min(s, b), sz)
    else:
        L = t.left

    if b > s:
        R = insert(t.right, max(s, a), b, sz)
    else:
        R = t.right

    # merge L, R
    t = merge(L, R)
    return t


def getLeaves(t, col):
    if t is None:
        return
    (a, b, s, sz) = t.data
    if s == -1:
        col.append((a, b, sz))
        return
    getLeaves(t.left, col)
    getLeaves(t.right, col)


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # to avoid much depth.
        intervals = [tuple(x) for x in intervals]
        intervals.sort()
        import random
        random.shuffle(intervals)

        # create tree from scratch.
        minstart = min(x[0] for x in intervals)
        maxend = max(x[1] for x in intervals)
        t = Tree(minstart, maxend + 1, -1, inf)

        # build tree and get leaves.
        for a, b in intervals:
            sz = (b - a + 1)
            t = insert(t, a, b + 1, sz)
        leaves = []
        getLeaves(t, leaves)

        # print tree and leaves.
        printT(t)
        print(leaves)

        ans = []
        for q in queries:
            s, e = 0, len(leaves) - 1
            while s <= e:
                m = (s + e) // 2
                if leaves[m][0] > q:
                    e = m - 1
                else:
                    s = m + 1
            # leaves[e][0] <= q
            if e == -1:
                ans.append(-1)
                continue

            (a, b, sz) = leaves[e]
            if q < b and sz != inf:
                ans.append(sz)
            else:
                ans.append(-1)
        return ans


class Solution2:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        for i in range(len(intervals)):
            (a, b) = intervals[i]
            e = (a, 0, i)
            events.append(e)
            e = (b, 2, i)
            events.append(e)

        for i in range(len(queries)):
            q = queries[i]
            e = (q, 1, i)
            events.append(e)

        events.sort()
        from sortedcontainers import SortedList
        ls = SortedList()
        retired = set()
        ans = [-1] * len(queries)

        # print(events)

        for (_, type, index) in events:
            if type == 1:  # query
                while ls and ls[0][1] in retired:
                    del ls[0]
                size = -1
                if ls:
                    size = ls[0][0]
                ans[index] = size

            elif type == 0:  # enqueue.
                size = intervals[index][1] - intervals[index][0] + 1
                ls.add((size, index))

            else:
                retired.add(index)

        return ans


cases = [
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
    ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
    ([[9, 9], [6, 7], [5, 6], [2, 5], [3, 3]], [6, 1, 1, 1, 9], [2, -1, -1, -1, 1]),
]

import aatest_helper

#
# for f in ('input.txt', 'input2.txt'):
#     import os
#
#     if not os.path.exists(f): continue
#     with open(f) as fh:
#         a = eval(fh.readline())
#         b = eval(fh.readline())
#         cases.append((a, b, aatest_helper.ANYTHING))

aatest_helper.run_test_cases(Solution2().minInterval, cases)

if __name__ == '__main__':
    pass
