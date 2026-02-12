#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        SUM = [0] * (n + 1)

        def updateSum(i):
            SUM[i] = cost[i - 1]
            if (2 * i + 1) > n: return
            updateSum(2 * i)
            updateSum(2 * i + 1)
            SUM[i] += max(SUM[2 * i], SUM[2 * i + 1])

        updateSum(1)
        # print(SUM)
        ans = 0

        def visit(i):
            nonlocal ans
            if (2 * i + 1) > n: return
            l = SUM[2 * i]
            r = SUM[2 * i + 1]
            ans += abs(l - r)
            visit(2 * i)
            visit(2 * i + 1)

        visit(1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (7, [1, 5, 2, 2, 3, 3, 1], 6),
    (3, [5, 3, 3, ], 0)
]

aatest_helper.run_test_cases(Solution().minIncrements, cases)

if __name__ == '__main__':
    pass
