#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        K = 3
        rs = [[] for _ in range(K)]
        for i, xs in enumerate(requirements):
            for k in range(K):
                rs[k].append((xs[k], i))
        for i in range(K):
            rs[i].sort(reverse=True)

        n = len(requirements)
        ok = [0] * n
        ans = [-1] * n

        xs = [0] * K
        increase.insert(0, [0] * K)
        for d, x in enumerate(increase):
            for k in range(K):
                xs[k] += x[k]

            for k in range(K):
                while rs[k] and rs[k][-1][0] <= xs[k]:
                    i = rs[k][-1][1]
                    ok[i] += 1
                    rs[k].pop()
                    if ok[i] == K:
                        ans[i] = d

        return ans


cases = [
    ([[2, 8, 4], [2, 5, 0], [10, 9, 8]], [[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]], [2, -1, 3, -1]),
    ([[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]], [[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]],
     [-1, 4, 3, 3, 3]),
    ([[1, 1, 1]], [[0, 0, 0]], [0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getTriggerTime, cases)
