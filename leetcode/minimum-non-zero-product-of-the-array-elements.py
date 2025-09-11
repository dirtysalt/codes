#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        # there is one item = (1 << p) - 1
        # and (2^(p-1) - 1 items = (1 << p) - 2
        # and (2^(p-1) - 1 items = 1
        if p == 1: return 1

        val = (1 << p) - 1
        MOD = 10 ** 9 + 7

        def pow(x, y):
            t = x
            ans = 1
            while y:
                ans = ans * t
                ans = ans % MOD
                if y % 2 == 1:
                    t = (t * t)
                    t = t % MOD
                y = y // 2
            return ans

        val = val * pow((1 << p) - 2, (1 << (p - 1)) - 1)
        val = val % MOD
        return val


true, false, null = True, False, None
cases = [
    (1, 1),
    (2, 6),
    (3, 1512)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minNonZeroProduct, cases)

if __name__ == '__main__':
    pass
