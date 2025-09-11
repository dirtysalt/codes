#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import collections

import functools
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def sqdist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        n = len(points)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j: continue

                sqdist_ij = sqdist(points[i], points[j])
                for k in range(j + 1, n):
                    if i == k: continue

                    sqdist_ik = sqdist(points[i], points[k])
                    print(i, j, k)
                    if sqdist_ij == sqdist_ik:
                        res += 1
        # i, j, k == i, k, j
        return res * 2


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def sqdist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        n = len(points)
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                v = sqdist(points[i], points[j])
                pairs.append((i, v))
                pairs.append((j, v))

        def cmp_fn(a, b):
            if a[1] == b[1]:
                return a[0] - b[0]
            return a[1] - b[1]

        pairs.sort(key=functools.cmp_to_key(cmp_fn))
        # print(pairs)

        res, cnt = 0, 1
        last_v, last_i = None, None
        for (i, value) in pairs:
            if value == last_v and last_i == i:
                cnt += 1
            else:
                res += cnt * (cnt - 1)
                cnt, last_v, last_i = 1, value, i
        res += cnt * (cnt - 1)
        return res


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def sqdist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        dist = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                v = sqdist(points[i], points[j])
                dist[v].append(i)
                dist[v].append(j)

        res = 0
        for v, pairs in dist.items():
            if len(pairs) == 1:
                continue
            pairs.sort()
            last_i, cnt = None, 1
            for i in pairs:
                if last_i == i:
                    cnt += 1
                else:
                    res += cnt * (cnt - 1)
                    last_i, cnt = i, 1
            res += cnt * (cnt - 1)

        return res


def test():
    cases = [
        ([[0, 0], [1, 0], [2, 0]], 2),
        ([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]], 20),
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (ps, exp) = c
        res = sol.numberOfBoomerangs(ps)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
