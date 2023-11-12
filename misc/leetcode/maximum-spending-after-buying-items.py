#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        n, m = len(values), len(values[0])
        st = [m - 1 for i in range(n)]
        ans = 0
        for d in range(n * m):
            k = 0
            for j in range(n):
                if st[j] == -1:
                    continue
                if st[k] == -1 or values[j][st[j]] < values[k][st[k]]:
                    k = j
            c = (d + 1) * values[k][st[k]]
            st[k] -= 1
            ans += c
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1], [1, 1]], 10),
    ([[8, 5, 2], [6, 4, 1], [9, 7, 3]], 285),
    ([[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]], 386),
]

aatest_helper.run_test_cases(Solution().maxSpending, cases)

if __name__ == '__main__':
    pass
