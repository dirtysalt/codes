#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        maxn = max(nums)
        n = len(nums)
        acc = [[0] * (maxn + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(maxn + 1):
                acc[i + 1][j] = acc[i][j]
            acc[i + 1][nums[i]] += 1

        ans = []
        inf = 1 << 30
        for l, r in queries:
            last = None
            val = inf
            for j in range(maxn + 1):
                c = acc[r + 1][j] - acc[l][j]
                if c != 0:
                    if last is not None:
                        res = j - last
                        val = min(val, res)
                    last = j
            if val == inf:
                val = -1
            ans.append(val)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]], [2, 1, 4, 1]),
    ([4, 5, 2, 2, 7, 10], [[2, 3], [0, 2], [0, 5], [3, 5]], [-1, 1, 1, 3])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDifference, cases)

if __name__ == '__main__':
    pass
