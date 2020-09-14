#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        citations.sort()
        if citations[-1] == 0:
            return 0

        s, e = 1, n
        while s <= e:
            h = (s + e) // 2
            check_idx = n - h
            if citations[check_idx] >= h:
                s = h + 1
            else:
                e = h - 1
        ans = e
        return ans


cases = [
    ([3, 0, 6, 1, 5], 3)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().hIndex, cases)
