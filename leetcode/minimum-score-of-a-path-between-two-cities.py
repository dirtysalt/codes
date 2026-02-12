#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class UnionFind:
    def __init__(self, values):
        r, c, = {}, {}
        for v in values:
            r[v], c[v] = v, 1
        self.r, self.c = r, c

    def size(self, a):
        ra = self.find(a)
        return self.c[ra]

    def find(self, a):
        if a not in self.r:
            self.r[a] = a
            self.c[a] = 1
            return a

        # find root.
        x = a
        while True:
            ra = self.r[x]
            if ra == x:
                break
            x = ra

        # compress path.
        x = a
        while x != ra:
            rx = self.r[x]
            self.r[x] = ra
            x = rx
        return ra

    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return ra
        ca, cb = self.c[ra], self.c[rb]
        if ca > cb:
            ca, cb, ra, rb = cb, ca, rb, ra
        self.r[ra] = rb
        self.c[rb] += ca
        return rb


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads.sort(key=lambda x: x[2])
        uf = UnionFind(list(range(1, n + 1)))
        inf = 1 << 30
        w = [inf] * (n + 1)
        for x, y, z in roads:
            w[x] = min(w[x], z)
            w[y] = min(w[y], z)
            px = uf.find(x)
            py = uf.find(y)
            z = uf.merge(px, py)
            w[z] = min(w[px], w[py])

        p1 = uf.find(1)
        pn = uf.find(n)
        if p1 != pn:
            return -1
        return w[p1]


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
    (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
]

aatest_helper.run_test_cases(Solution().minScore, cases)

if __name__ == '__main__':
    pass
