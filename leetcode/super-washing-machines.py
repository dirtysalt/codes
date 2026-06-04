#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        S = sum(machines)
        n = len(machines)
        if S % n != 0:
            return -1
        avg = S // n
        acc = 0
        ans = 0
        for x in machines:
            adjust = x - avg
            acc += adjust
            ans = max(ans, adjust, abs(acc))
        return ans


cases = [
    ((1, 0, 5), 3),
    ((0, 3, 0), 2),
    ((0, 2, 0), -1),
    ([9, 1, 8, 8, 9], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMinMoves, cases)
