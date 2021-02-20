#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import Counter
        cnt = Counter()
        for x, y in roads:
            cnt[x] += 1
            cnt[y] += 1
        rs = set((x, y) if x < y else (y, x) for (x, y) in roads)
        ans = 0
        for x in range(n):
            for y in range(x + 1, n):
                v = cnt[x] + cnt[y]
                if (x, y) in rs or (y, x) in rs:
                    v -= 1
                ans = max(ans, v)
        return ans


cases = [
    (4, [[0, 1], [0, 3], [1, 2], [1, 3]], 4),
    (5, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]], 5),
    (8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]], 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximalNetworkRank, cases)
