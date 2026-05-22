#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0

        acc = 0
        for x in arr:
            acc += x
            ans = max(ans, acc)
            if acc < 0:
                acc = 0

        if k == 1:
            return ans

        rmax = 0
        acc = 0
        for x in reversed(arr):
            acc += x
            rmax = max(rmax, acc)
        lmax = 0
        acc = 0
        for x in arr:
            acc += x
            lmax = max(lmax, acc)

        lr = lmax + rmax
        lr += (k - 2) * max(acc, 0)
        ans = max(ans, lr)
        ans = ans % MOD
        return ans


cases = [
    ([1, -2, 1], 5, 2),
    ([-1, -2], 7, 0),
    ([1, 2], 3, 9),
    ([-5, -2, 0, 0, 3, 9, -2, -5, 4], 5, 20)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kConcatenationMaxSum, cases)
