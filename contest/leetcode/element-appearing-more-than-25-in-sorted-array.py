#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        sz = n // 4 + 1

        for i in range(n - sz + 1):
            if arr[i] == arr[i + sz - 1]:
                return arr[i]

        return arr[0]


cases = [
    ([1, 2, 2, 6, 6, 6, 6, 7, 10], 6),
    ([1, 2, 3, 3], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findSpecialInteger, cases)
