#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind = [0] * n
        for x, y in edges:
            ind[y] += 1
        ans = [i for i in range(n) if ind[i] == 0]
        return ans


cases = [
    (6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]], [0, 3]),
    (5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]], [0, 2, 3]),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().findSmallestSetOfVertices, cases)
