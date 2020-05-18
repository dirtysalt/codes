#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:



cases = [
    ([1, 0, 5], 3),
    ([0, 3, 0], 2),
    ([0, 2, 0], -1),
    ([0, 0, 0, 4], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMinMoves, cases)
