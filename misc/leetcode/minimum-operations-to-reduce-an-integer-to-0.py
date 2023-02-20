#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minOperations(self, n: int) -> int:
        from collections import deque
        q = deque()
        vis = set()
        q.append((n, 0))
        vis.add(n)

        def extend(x):
            d = x & (x - 1)
            if d == 0:
                return [0]
            return [d, x + (x - d)]

        while q:
            (x, y) = q.popleft()
            if x == 0: return y
            vis.add(x)
            for z in extend(x):
                if z not in vis:
                    vis.add(z)
                    q.append((z, y + 1))


true, false, null = True, False, None
import aatest_helper

cases = [
    (39, 3),
    (54, 3),
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
