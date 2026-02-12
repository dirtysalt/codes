#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Item:
    def __init__(self, x, c):
        self.x = x
        self.c = c

    def __lt__(self, o):
        return self.x > o.x


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        hp = []
        courses.sort(key=lambda x: x[1])

        acc = 0
        for c in courses:
            t, d = c
            if acc + t <= d:
                heapq.heappush(hp, Item(t, c))
                acc += t
                continue

            if hp and hp[0].x > t:
                acc += t - hp[0].x
                heapq.heapreplace(hp, Item(t, c))

        print(sorted([x.c for x in hp], key=lambda x: x[1]))

        ans = len(hp)
        return ans


cases = [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2], [2, 3]], 2),
    ([[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]], 4),
    ([[7, 16], [2, 3], [3, 12], [3, 14], [10, 19], [10, 16], [6, 8], [6, 11], [3, 13], [6, 16]], 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().scheduleCourse, cases)
