#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        diff = target.copy()
        for i in range(1, n):
            diff[i] = target[i] - target[i - 1]

        ans = 0
        for i in range(n):
            if diff[i] > 0:
                ans += diff[i]

        debug = False
        if debug:
            ops = []
            t = 0
            while t < n:
                if diff[t] < 0: break
                t += 1

            for i in range(n):
                while diff[i] > 0:
                    diff[i] -= 1
                    while t < n and diff[t] >= 0:
                        t += 1
                    if t < n:
                        diff[t] += 1
                    ops.append((i, t - 1))

            # print(ans, ops)
            assert len(ops) == ans
        return ans


cases = [
    ([1, 2, 3, 2, 1], 3),
    ([3, 1, 1, 2], 4),
    ([3, 1, 5, 4, 2], 7),
    ([1, 1, 1, 1], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minNumberOperations, cases)
