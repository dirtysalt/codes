#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        exp = 0
        split = False
        hi, lo = 1, 1
        MOD = 10 ** 12
        assert (MOD * (10 ** 6) < (2 ** 63) - 1)
        for x in range(left, right + 1):
            lo = lo * x
            while lo % 10 == 0:
                exp += 1
                lo = lo // 10

            if lo >= (10 ** 10):
                split = True

            hi = hi * x

            if lo >= MOD:
                lo = lo % MOD

            while hi >= MOD:
                hi = hi // 10

        if not split:
            return '%se%s' % (lo, exp)
        else:
            MOD = 10 ** 5
            lo = lo % MOD
            while hi >= MOD:
                hi = hi // 10
            return '%05d...%05de%s' % (hi, lo, exp)


true, false, null = True, False, None
cases = [
    (1, 4, "24e0"),
    (2, 11, "399168e2"),
    (999998, 1000000, "99999...00002e6"),
    (256, 65535, "23510...78528e16317"),
    (410, 70833, "81384...08512e17604"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().abbreviateProduct, cases)

if __name__ == '__main__':
    pass
