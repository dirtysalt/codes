#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def is_prime(x):
            if x == 1:
                return False
            i = 2
            while i * i <= x:
                for j in range(i, x // i + 1):
                    if i * j == x:
                        return False
                i += 1
            return True

        P = 10 ** 9 + 7
        a, b, ans = 0, 0, 1
        for i in range(1, n + 1):
            if is_prime(i):
                a += 1
                ans = (ans * a) % P
            else:
                b += 1
                ans = (ans * b) % P

        return ans


cases = [
    (5, 12),
    (100, 682289015)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().numPrimeArrangements, cases)
