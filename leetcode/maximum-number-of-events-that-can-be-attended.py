#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# note(yan): 难以解释的贪心算法!!
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        added = set()
        ans = 0

        for ev in events:
            (s, e) = ev
            for d in range(s, e + 1):
                if d not in added:
                    added.add(d)
                    ans += 1
                    break
        return ans


cases = [
    ([[1, 2], [2, 3], [3, 4], [1, 2]], 4),
    ([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]], 4),
    ([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]], 7),
    ([[1, 100000]], 1),
    ([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]], 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxEvents, cases)
