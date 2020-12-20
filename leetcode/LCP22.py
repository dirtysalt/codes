#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        C = [[0] * (n + 1) for _ in range(n + 1)]
        C[0][0] = 1
        for i in range(1, n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
                # print('C(%d, %d) = %d' % (i, j, C[i][j]))

        ans = 0
        for x in range(n):
            for y in range(n):
                p = (x + y) * n - x * y
                if p == k:
                    # print(x, y, p, k)
                    ans += C[n][x] * C[n][y]
        if n * n == k:
            ans += 1
        return ans


cases = [
    (2, 2, 4),
    (2, 1, 0),
    (2, 4, 1),
    (3, 8, 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().paintingPlan, cases)
