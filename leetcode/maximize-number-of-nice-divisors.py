#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        import math
        n = primeFactors

        def split(k):
            if k == 0 or k > n: return 0
            avg = n // k
            r = n - k * avg
            # there are (r) (avg+1) , and (k-r) avg
            # ravg + r + kavg - ravg = r + kavg = n
            value = r * math.log2(avg + 1) + (k - r) * math.log2(avg)
            # print(k, avg, r, value, 2 ** value)
            return value

        def test():
            s, e = 1, n
            while s < e:
                m = (s + e) // 2
                # print(s, e, m)
                a = split(m - 1)
                b = split(m)
                c = split(m + 1)
                if b > a and b > c:
                    return m
                if a <= c:
                    s = m + 1
                else:
                    e = m - 1
            return s

        MOD = 10 ** 9 + 7

        # b ^ t
        def mul(b, t):
            ans = 1
            while t:
                if t & 0x1:
                    ans = ans * b
                    ans = ans % MOD
                t = t >> 1
                b = b * b
                b = b % MOD
            return ans

        k = test()
        avg = n // k
        r = n - avg * k
        ans = 1 * mul(avg + 1, r)
        ans = ans % MOD
        ans = ans * mul(avg, k - r)
        ans = ans % MOD
        return ans


cases = [
    (1, 1),
    (5, 6),
    (8, 18),
    (18, 729),
    (9, 27),
    (73, 572712676),
    (545918790, 421090465)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxNiceDivisors, cases)
