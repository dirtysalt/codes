#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

import aatest_helper


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        rem = 0
        for x in A:
            rem = (rem << 1) + x
            rem = rem % 5
            res.append(rem == 0)
        return res


sol = Solution()
true = True
false = False
cases = [
    ([0, 1, 1], [true, false, false]),
    ([1, 1, 1], [false, false, false]),
    ([0, 1, 1, 1, 1, 1], [true, false, false, false, true, false]),
    ([1, 1, 1, 0, 1], [false, false, false, false, false]),
]

aatest_helper.run_test_cases(sol.prefixesDivBy5, cases)
