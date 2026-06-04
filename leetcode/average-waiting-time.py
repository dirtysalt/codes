#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = 0
        now = 0
        for a, t in customers:
            ans += max(now - a, 0) + t
            now = max(now, a) + t
        avg = round(ans / len(customers), 6)
        return avg


cases = [
    ([[1, 2], [2, 5], [4, 3]], 5.0),
    ([[5, 2], [5, 4], [10, 3], [20, 1]], 3.25)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().averageWaitingTime, cases)
