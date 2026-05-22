#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def GCD(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def LCM(a, b):
            return a * b // GCD(a, b)

        def test(k):
            lcm = LCM(divisor1, divisor2)
            # be used to g1 and g2 both
            a = k - k // divisor1 - k // divisor2 + k // lcm
            # only to g1
            b = (k - k // divisor1) - a
            # only to g2
            c = (k - k // divisor2) - a

            if (b + a) < uniqueCnt1: return False
            r = min(a, (b + a) - uniqueCnt1)
            if (r + c) < uniqueCnt2: return False
            return True

        s, e = 1, (uniqueCnt1 + uniqueCnt2) * 2
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    (2, 7, 1, 3, 4),
    (3, 5, 2, 1, 3),
    (2, 4, 8, 2, 15),
    (12, 3, 2, 10, 14),
]

aatest_helper.run_test_cases(Solution().minimizeSet, cases)

if __name__ == '__main__':
    pass
