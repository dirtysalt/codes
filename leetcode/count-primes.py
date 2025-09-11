#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0

        ps = [0] * n
        for i in range(2, n):
            if i * i >= n: break
            if ps[i] == 1: continue
            for j in range(i, (n - 1) // i + 1):
                ps[i * j] = 1

        ans = 0
        for i in range(2, n):
            if ps[i] == 0:
                ans += 1
        return ans


cases = [
    (10, 4),
    (0, 0),
    (1, 0),
    (2, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPrimes, cases)
