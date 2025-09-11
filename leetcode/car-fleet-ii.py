#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        class Range:
            def __init__(self, s, e, pos, speed):
                self.s = s
                self.e = e
                self.pos = pos
                self.speed = speed
                self.t = 0

        rs = []
        n = len(cars)
        for i in range(n):
            r = Range(i, i, cars[i][0], cars[i][1])
            rs.append(r)

        ans = [-1.0] * n
        mark = [0] * n
        hp = []
        import heapq

        def update(x, now):
            a = rs[x]
            b = rs[x + 1]
            assert now >= a.t
            assert now >= b.t
            pa = a.pos + (now - a.t) * a.speed
            pb = b.pos + (now - b.t) * b.speed
            if pa < pb and a.speed > b.speed:
                t = (pb - pa) / (a.speed - b.speed)
                heapq.heappush(hp, (t + now, x))

        for i in range(n - 1):
            update(i, 0)

        Gt = 0
        while hp:
            (t, i) = heapq.heappop(hp)
            if t < Gt: continue
            if mark[i]: continue
            ans[i] = round(t, 5)
            mark[i] = 1
            Gt = t

            # collision rs[i] and rs[i+1]
            a, b = rs[i], rs[i + 1]
            s, e = a.s, b.e
            assert t >= a.t and t >= b.t, (t, a.t, b.t)
            pa = a.pos + (t - a.t) * a.speed
            pb = b.pos + (t - b.t) * b.speed
            assert abs(pa - pb) < 1e-6, (pa, pb)
            speed = min(a.speed, b.speed)
            r = Range(s, e, pa, speed)
            r.t = t
            rs[s] = rs[e] = r

            if (s - 1) >= 0:
                update(s - 1, t)
            if (e + 1) < n:
                update(e, t)

        return ans


cases = [
    ([[1, 2], [2, 1], [4, 3], [7, 2]], [1.00000, -1.00000, 3.00000, -1.00000]),
    ([[3, 4], [5, 4], [6, 3], [9, 1]], [2.00000, 1.00000, 1.50000, -1.00000]),
    (
        [[1, 4], [4, 5], [7, 1], [13, 4], [14, 3], [15, 2], [16, 5], [19, 1]],
        [2.0, 0.75, -1.0, 1.0, 1.0, 4.0, 0.75, -1.0]),
    ([[1, 5], [6, 5], [7, 5], [14, 5], [15, 3], [16, 4], [17, 5], [18, 1], [19, 2], [20, 2]],
     [4.25, 3.0, 2.75, 0.5, 1.5, 0.66667, 0.25, -1.0, -1.0, -1.0]),
    ([[1, 5], [6, 5], [7, 5], [14, 5], [15, 3], [16, 4], [17, 5], [18, 1], [19, 2], [20, 2]],
     [4.25, 3.0, 2.75, 0.5, 1.5, 0.66667, 0.25, -1.0, -1.0, -1.0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getCollisionTimes, cases)
