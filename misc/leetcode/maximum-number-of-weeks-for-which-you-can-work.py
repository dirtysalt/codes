#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        acc = sum(milestones)
        a = milestones[-1]
        b = acc - a
        if b < a:
            return 2 * b + 1
        else:
            return acc


true, false, null = True, False, None
cases = [
    ([1, 2, 3], 6),
    ([5, 2, 1], 7),
    ([9, 3, 6, 8, 2, 1], 29)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfWeeks, cases)

if __name__ == '__main__':
    pass
