#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        first = list(range(n))
        last = list(range(n))
        mark = [0] * n

        def queryFirst(x):
            p = x
            while first[p] != p:
                p = first[p]

            while first[x] != p:
                x2 = first[x]
                first[x] = p
                x = x2

            return p

        def queryLast(x):
            x = queryFirst(x)
            p = x
            while last[p] != p:
                p = last[p]

            while last[x] != p:
                x2 = last[x]
                last[x] = p
                x = x2
            return p

        cnt = 0
        ans = -1

        for step, x in enumerate(arr):
            x = x - 1
            mark[x] = 1

            if x > 0 and mark[x - 1]:
                p0 = queryFirst(x - 1)
                if (x - p0) == m:
                    cnt -= 1
                first[x] = p0
                last[p0] = x

            if x < (n - 1) and mark[x + 1]:
                p1 = queryLast(x + 1)
                if (p1 - x) == m:
                    cnt -= 1
                first[p1] = x
                last[x] = p1

            p0 = queryFirst(x)
            p1 = queryLast(x)
            if (p1 - p0 + 1) == m:
                cnt += 1
            if cnt > 0:
                ans = step + 1

        return ans


cases = [
    ([3, 5, 1, 2, 4], 1, 4),
    ([3, 1, 5, 4, 2], 2, -1),
    ([1], 1, 1),
    ([2, 1], 2, 2),
    ([3, 2, 5, 6, 10, 8, 9, 4, 1, 7], 3, 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findLatestStep, cases)
