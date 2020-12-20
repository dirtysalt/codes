#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x, y):
            return x * y // gcd(x, y)

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        if a == b == c:
            return a * n

        def test(abc):
            a, b, c = abc
            Gab = lcm(a, b)
            Gac = lcm(a, c)
            Gbc = lcm(b, c)
            Gabc = lcm(Gab, c)

            s, e = 1, n
            found = False
            while s <= e:
                m = (s + e) // 2
                x = m + (a * m) // b + (a * m) // c
                y = (a * m) // Gab + (a * m) // Gac + (a * m) // Gbc
                z = (a * m) // Gabc
                seq = x - y + z
                if seq == n:
                    found = True
                    break
                elif seq > n:
                    e = m - 1
                else:
                    s = m + 1
            return found, a * m

        for x in ([a, b, c], [b, a, c], [c, a, b]):
            ok, ans = test(x)
            if ok:
                return ans


cases = [
    (3, 2, 3, 5, 4),
    (4, 2, 3, 4, 6),
    (1000000000, 2, 217983653, 336916467, 1999999984),
    (8, 5, 7, 3, 14),
    (5, 2, 3, 3, 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().nthUglyNumber, cases)
