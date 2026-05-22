#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# 费马小定理, 但是这里必须确保MOD是质数
# b^MOD % MOD = b
# b^(MOD-1) % MOD = 1
# b^(MOD-2) % MOD = (b^-1) % MOD
def pow_mod(a, b, MOD):
    res = 1
    while b:
        if b & 0x1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b = b >> 1
    return res


def div_mod(b, MOD):
    return pow_mod(b, MOD - 2, MOD)


def fac_mod(n, MOD):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % MOD
    return res


class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10 ** 9 + 7

        gap = []
        middle = []
        for i in range(1, len(sick)):
            g = sick[i] - sick[i - 1] - 1
            if g > 0:
                middle.append(g)
                gap.append(g)

        if sick[0] != 0:
            gap.append(sick[0])
        if sick[-1] != n - 1:
            gap.append(n - 1 - sick[-1])

        # print(gap, middle)

        ans = 1
        for x in middle:
            ans *= pow_mod(2, x - 1, MOD)
            ans %= MOD

        ans *= fac_mod(sum(gap), MOD)
        ans %= MOD

        for g in gap:
            r = fac_mod(g, MOD)
            ans *= div_mod(r, MOD)
            ans %= MOD

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [0, 4], 4),
    (4, [1], 3),
]

aatest_helper.run_test_cases(Solution().numberOfSequence, cases)

if __name__ == '__main__':
    pass
