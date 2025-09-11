#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r = 0, 0
        n = len(costs)
        from sortedcontainers import SortedList
        sl = SortedList()
        pos = SortedList()
        mask = [0] * n

        def add(p):
            pos.add(p)
            mask[p] = 1
            sl.add((costs[p], p))

        for p in range(candidates):
            if mask[p]: continue
            l = p
            add(p)

        for p in range(candidates):
            p2 = n - 1 - p
            if mask[p2]: continue
            r = p2
            add(p2)

        def nextp(p, l, r):
            i = pos.index(p)
            pos.remove(p)

            if i < candidates:
                while l < r and mask[l]: l += 1
                p = l
            else:
                while l < r and mask[r]: r -= 1
                p = r
            return p, l, r

        ans = 0
        for round in range(k):
            (c, p) = sl.pop(0)
            ans += c
            p, l, r = nextp(p, l, r)
            if mask[p]: continue
            add(p)
        return ans


true, false, null = True, False, None
cases = [
    ([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4, 11),
    ([1, 2, 4, 1], 3, 3, 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().totalCost, cases)

if __name__ == '__main__':
    pass
