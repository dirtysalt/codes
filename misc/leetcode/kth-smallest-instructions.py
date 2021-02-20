#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        n, m = destination
        steps = n + m
        n, m = n + 1, m + 1
        C = [[0] * n for _ in range(n + m)]
        C[0][0] = 1
        for i in range(1, n + m):
            for j in range(n):
                C[i][j] = C[i - 1][j] + (C[i - 1][j - 1] if j > 0 else 0)

        ans = []
        v, h = destination
        k -= 1
        for i in range(steps):
            # choose H first.
            x = C[h - 1 + v][v]
            if k < x:
                h -= 1
                ans.append('H')
            else:
                k -= x
                v -= 1
                ans.append('V')

        ans = ''.join(ans)
        return ans


cases = [
    ([1, 1], 1, "HV"),
    ([2, 3], 1, "HHHVV"),
    ([2, 3], 2, "HHVHV"),
    ([2, 3], 3, "HHVVH"),
    ([15, 2], 136, "VVVVVVVVVVVVVVVHH"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kthSmallestPath, cases)
