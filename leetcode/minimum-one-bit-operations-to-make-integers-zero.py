#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        cache = {}

        def fun(x):
            if x == 0: return 0
            key = x
            if key in cache: return cache[key]

            ans = 0
            y = 0
            for msb in reversed(range(32)):
                if (x >> msb) & 0x1 != (y >> msb) & 0x1:
                    if msb == 0:
                        ans += 1
                    else:
                        ans += 1 + fun(1 << (msb - 1))
                        y = 1 << (msb - 1)

            cache[key] = ans
            return ans

        ans = fun(n)
        return ans


cases = [
    (0, 0),
    (3, 2),
    (6, 4),
    (9, 14),
    (333, 393),
    (1 << 30, 2147483647)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumOneBitOperations, cases)
