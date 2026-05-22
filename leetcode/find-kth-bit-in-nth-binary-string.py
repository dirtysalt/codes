#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def query(n, k):
            if n == 1:
                return 0
            b = 1 << (n - 1)
            if k == b:
                return 1
            if k < b:
                return query(n - 1, k)
            ans = query(n - 1, 2 * b - k)
            return 1 - ans

        ans = query(n, k)
        return str(ans)


cases = [
    (3, 1, '0'),
    (4, 11, '1'),
    (1, 1, '0'),
    (2, 3, '1'),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findKthBit, cases)
