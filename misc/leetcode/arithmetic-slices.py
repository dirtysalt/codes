#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n == 0:
            return 0

        def f(sz):
            # print(sz)
            # 3 * (sz - 3 + 1) + 4 * (sz - 4 + 1) + ... + sz * 1
            # (sz - 2) + (sz - 3) + ... 1
            res = (sz - 1) * (sz - 2) // 2
            return res

        p = 0
        ans = 0
        for i in range(1, n - 1):
            if (A[i + 1] - A[i]) == (A[i] - A[i - 1]):
                continue

            # from p to i
            sz = (i + 1 - p)
            ans += f(sz)
            p = i

        sz = (n - p)
        ans += f(sz)

        return ans


cases = [
    ([1, 2, 3, 4], 3),
    ([1, 2, 3, 4, 7, 8, 9], 4),
    ([0, 0, 0, 0, 0], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfArithmeticSlices, cases)
