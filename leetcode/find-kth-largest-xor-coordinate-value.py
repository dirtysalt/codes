#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        temp = []
        last = [0] * m
        for i in range(n):
            t = matrix[i].copy()
            for j in range(1, m):
                t[j] ^= t[j - 1]
            for j in range(m):
                last[j] ^= t[j]
            temp.extend(last)

        temp.sort(reverse=True)
        # print(temp)
        ans = temp[k - 1]
        return ans


cases = [
    ([[5, 2], [1, 6]], 1, 7),
    ([[5, 2], [1, 6]], 2, 5),
    ([[5, 2], [1, 6]], 3, 4),
    ([[5, 2], [1, 6]], 4, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kthLargestValue, cases)
