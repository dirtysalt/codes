#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        seq = []
        for xs in grid:
            c = 0
            for x in reversed(xs):
                if x == 0:
                    c += 1
                else:
                    break
            seq.append(c)

        n = len(grid)
        ans = 0
        for i in range(n):
            exp = n - 1 - i
            k = None
            for j in range(len(seq)):
                if seq[j] >= exp:
                    k = j
                    break
            if k is None:
                return -1
            ans += k
            seq = seq[:k] + seq[k + 1:]
        return ans


cases = [
    ([[0, 0, 1], [1, 1, 0], [1, 0, 0]], 3),
    ([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]], -1),
    ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSwaps, cases)
