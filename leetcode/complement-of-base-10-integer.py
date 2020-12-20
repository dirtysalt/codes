#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        msb = 0
        n = N
        while n:
            msb += 1
            n = n >> 1
        msb = max(msb, 1)

        ans = (1 << msb) - 1 - N
        return ans


cases = [
    (5, 2),
    (0, 1),
    (10, 5),
    (7, 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().bitwiseComplement, cases)
