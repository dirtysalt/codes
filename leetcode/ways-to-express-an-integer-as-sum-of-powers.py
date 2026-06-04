#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


@functools.cache
def search(N, ni, x):
    if N == 0: return 1
    ans = 0
    for i in range(ni, N + 1):
        v = i ** x
        if v > N: break
        ans += search(N - v, i + 1, x)
    return ans


class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        ans = search(n, 1, x)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    (10, 2, 1),
    (4, 1, 2),
    (300, 1, aatest_helper.ANYTHING),
    (300, 2, aatest_helper.ANYTHING),
    (300, 3, aatest_helper.ANYTHING),
    (300, 4, aatest_helper.ANYTHING),
    (300, 5, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().numberOfWays, cases)

if __name__ == '__main__':
    pass
