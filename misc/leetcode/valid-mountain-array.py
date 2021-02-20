#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False

        idx = n
        for i in range(1, n):
            if A[i-1] == A[i]:
                return False

            if A[i - 1] > A[i]:
                idx = i
                break

        if idx == 1 or idx == n:
            return False

        for j in range(idx, n):
            if A[j - 1] <= A[j]:
                return False
        return True


cases = [
    # ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], False),
    ([1, 3, 2], True)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().validMountainArray, cases)
