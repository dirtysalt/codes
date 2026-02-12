#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        C = [[0] * (n + 1) for _ in range(n + 1)]
        C[0][0] = 1
        for i in range(1, n + 1):
            C[i][0] = 1
            C[i][i] = 1
            for j in range(1, i):
                C[i][j] = C[i - 1][j] + C[i - 1][j - 1]

        def test(xs):
            if len(xs) in (0, 1): return 1
            a, b = [], []
            for i in range(1, len(xs)):
                if xs[i] > xs[0]:
                    b.append(xs[i])
                else:
                    a.append(xs[i])

            sa = test(a)
            sb = test(b)
            return C[len(a) + len(b)][len(a)] * sa * sb

        ans = test(nums)
        MOD = 10 ** 9 + 7
        ans = (ans - 1) % MOD
        return ans


cases = [
    ([2, 1, 3], 1),
    ([3, 4, 5, 1, 2], 5),
    ([1, 2, 3], 0),
    ([3, 1, 2, 5, 4, 6], 19),
    ([9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18], 216212978),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numOfWays, cases)
