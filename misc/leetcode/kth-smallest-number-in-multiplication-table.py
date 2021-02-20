#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m

        def testOrder(x):
            order = 0
            for i in range(1, m + 1):
                c = min(n, x // i)
                if c == 0:
                    break
                order += c
            return order

        s, e = 1, m * n
        while s <= e:
            x = (s + e) // 2
            order = testOrder(x)
            # print(x, order)
            if order < k:
                s = x + 1
            else:
                e = x - 1

        ans = s
        return ans


cases = [
    (3, 3, 5, 3),
    (2, 3, 6, 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findKthNumber, cases)
