#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        MAX = sum(cost)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + time[i]

        from functools import cache
        @cache
        def search(i, t):
            if (t + acc[-1] - acc[i]) < 0: return MAX
            if t >= (n - i): return 0

            # what if paid
            a = search(i + 1, t + time[i]) + cost[i]
            # what if free
            b = search(i + 1, t - 1)
            ans = min(a, b)
            return ans

        ans = search(0, 0)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 2], [1, 2, 3, 2], 3),
    ([2, 3, 4, 2], [1, 1, 1, 1], 4),
    ([2, 2], [1, 1], 2),
    ([42, 8, 28, 35, 21, 13, 21, 35], [2, 1, 1, 1, 2, 1, 1, 2], 63),
]
cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().paintWalls, cases)

if __name__ == '__main__':
    pass
