#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        hs = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    hs[j] = 0
                    continue

                hs[j] += 1
                h = hs[j]
                for k in reversed(range(j + 1)):
                    h = min(h, hs[k])
                    ans += h
                    if h == 0:
                        break
        return ans


cases = [
    ([[1, 0, 1],
      [1, 1, 0],
      [1, 1, 0]], 13),
    ([[0, 1, 1, 0],
      [0, 1, 1, 1],
      [1, 1, 1, 0]], 24),
    ([[1, 1, 1, 1, 1, 1]], 21),
    ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numSubmat, cases)
