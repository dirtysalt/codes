#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        hs = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    hs[j] += 1
                else:
                    hs[j] = 0

            tmp = hs.copy()
            tmp.sort(reverse=True)
            for j in range(m):
                area = (j + 1) * tmp[j]
                ans = max(ans, area)

        return ans


cases = [
    ([[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4),
    ([[1, 0, 1, 0, 1]], 3),
    ([[1, 1, 0], [1, 0, 1]], 2),
    ([[0, 0], [0, 0]], 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestSubmatrix, cases)
