#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        i = 0
        ans = 0
        while i < n:
            j = i
            while j + 1 < n and A[j + 1] > A[j]:
                j += 1
            k = j
            while j + 1 < n and A[j + 1] < A[j]:
                j += 1
            # print(i, k, j)
            # i.. k .. j
            if i < k < j:
                ans = max(ans, j - i + 1)

            if k == j:
                i = j + 1
            else:
                i = j
        return ans


cases = [
    ([2, 1, 4, 7, 3, 2, 5], 5),
    ([2, 2, 2], 0)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().longestMountain, cases)
