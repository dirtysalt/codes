#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        first = list(range(n))
        size = [1] * n
        mark = [0] * n
        from collections import Counter
        cnt = Counter()

        def queryFirst(x):
            p = x
            while first[p] != p:
                p = first[p]

            # compress.
            while first[x] != p:
                x2 = first[x]
                first[x] = p
                x = x2

            return p

        def merge(a, b):
            pa = queryFirst(a)
            pb = queryFirst(b)
            if pa != pb:
                if pa < pb:
                    pa, pb = pb, pa
                cnt[size[pa]] -= 1
                cnt[size[pb]] -= 1
                size[pb] = size[pa] + size[pb]
                first[pa] = pb
                cnt[size[pb]] += 1

        ans = -1

        for step, x in enumerate(arr):
            x = x - 1
            mark[x] = 1
            cnt[1] += 1

            if x > 0 and mark[x - 1]:
                merge(x, x - 1)

            if x < (n - 1) and mark[x + 1]:
                merge(x, x + 1)

            if cnt[m] > 0:
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
