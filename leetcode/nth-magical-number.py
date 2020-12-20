#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        C = A * B // gcd(A, B)

        def test(A, B, C):
            s, e = 1, N
            while s <= e:
                m = (s + e) // 2
                value = m * A
                b = value // B
                c = value // C
                order = m + b - c
                if order == N:
                    return value
                elif order > N:
                    e = m - 1
                else:
                    s = m + 1

            return -1

        ans = test(A, B, C)
        if ans == -1:
            ans = test(B, A, C)
        MOD = 10 ** 9 + 7
        return ans % MOD


cases = [
    (1, 2, 3, 2),
    (4, 2, 3, 6),
    (5, 2, 4, 10),
    (3, 6, 4, 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().nthMagicalNumber, cases)
