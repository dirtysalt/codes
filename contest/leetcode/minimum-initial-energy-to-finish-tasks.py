#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tmp = []
        for a, m in tasks:
            tmp.append((a, m))

        def keyFn(x):
            a, m = x
            return -(m - a)

        tmp.sort(key=keyFn)
        # print(tmp)

        ans = 0
        acc = 0
        for a, m in tmp:
            ans = max(ans, acc + m)
            acc += a
        return ans


cases = [
    ([[1, 2], [2, 4], [4, 8]], 8),
    ([[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]], 32),
    ([[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]], 27)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumEffort, cases)
