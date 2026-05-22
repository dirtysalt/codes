#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        indices = [-1] * 101
        for i in range(len(pieces)):
            for p in pieces[i]:
                indices[p] = i

        used = [0] * 101
        tmp = []
        for x in arr:
            j = indices[x]
            if j == -1: return False
            if used[j]: continue
            used[j] = 1
            tmp.extend(pieces[j])

        return tmp == arr


cases = [
    ([85], [[85]], True),
    ([15, 88], [[88], [15]], True),
    ([49, 18, 16], [[16, 18, 49]], False),
    ([91, 4, 64, 78], [[78], [4, 64], [91]], True),
    ([1, 3, 5, 7], [[2, 4, 6, 8]], False),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canFormArray, cases)
