#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        K = 2
        xs = []
        xs += [(A[i][0], 0) for i in range(len(A))]
        xs += [(A[i][1], 1) for i in range(len(A))]
        xs += [(B[i][0], 0) for i in range(len(B))]
        xs += [(B[i][1], 1) for i in range(len(B))]
        xs.sort()

        ans = []
        last = None
        depth = 0
        for p, d in xs:
            if d == 0:
                depth += 1
                if depth == K:
                    last = p
            else:
                depth -= 1
                if last is None:
                    continue
                assert depth == K - 1
                ans.append([last, p])
                last = None
        return ans


cases = [
    ([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]],
     [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]),
    ([[5, 10]], [[5, 6]], [[5, 6]]),
    ([[14, 16]], [[7, 13], [16, 20]], [[16, 16]]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().intervalIntersection, cases)
