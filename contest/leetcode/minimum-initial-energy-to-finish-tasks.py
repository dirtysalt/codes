#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tmp = []
        for a, m in tasks:
            tmp.append((m - a, m, a))
        tmp.sort()
        ans = 0
        for _, m, a in tmp:
            ans = max(ans, m - a) + a
        return ans


cases = [
    ([[1, 2], [2, 4], [4, 8]], 8),
    ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32),
    ([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumEffort, cases)
