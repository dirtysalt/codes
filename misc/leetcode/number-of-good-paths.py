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
            return
        ca, cb = self.c[ra], self.c[rb]
        if ca > cb:
            ca, cb, ra, rb = cb, ca, rb, ra
        self.r[ra] = rb
        self.c[rb] += ca


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        from collections import defaultdict
        dd = defaultdict(list)
        for i in range(n):
            v = vals[i]
            dd[v].append(i)
        values = list(dd.keys())
        values.sort()
        edges.sort(key=lambda x: -max(vals[x[0]], vals[x[1]]))

        fu = UnionFind(list(range(n)))
        ans = 0
        for v in values:
            while edges:
                x, y = edges[-1]
                ev = max(vals[x], vals[y])
                if ev == v:
                    fu.merge(x, y)
                    edges.pop()
                else:
                    break

            from collections import Counter
            cnt = Counter()
            for x in dd[v]:
                p = fu.find(x)
                cnt[p] += 1
            # print(v, dd[v], cnt)
            for c in cnt.values():
                ans += c * (c + 1) // 2
        return ans


true, false, null = True, False, None
cases = [
    ([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]], 6),
    ([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]], 7),
    ([1], [], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfGoodPaths, cases)

if __name__ == '__main__':
    pass
