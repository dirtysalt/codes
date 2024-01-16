#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def fast(N, x):
    ans, one, bu = 0, 0, 0
    while (1 << bu) <= N:
        bu += 1
    for b in reversed(range(bu)):
        if (N >> b) & 0x1:
            b1 = (1 << b)
            r0 = one * b1
            r1 = (b // x) * (b1 // 2)
            if (b + 1) % x == 0:
                one += 1
            ans += r0 + r1
    ans += one
    return ans


def slow(N, x):
    ans = 0
    for n in range(1, N + 1):
        c = 0
        b = x
        while (1 << (b - 1)) <= n:
            if (n >> (b - 1)) & 0x1:
                c += 1
            b += x
        ans += c
    return ans


def check():
    for N in range(1, 100):
        a = fast(N, 2)
        b = slow(N, 2)
        if a != b:
            print(N, a, b)


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        s, e = 1, (1 << 63)
        while s <= e:
            m = (s + e) // 2
            r = fast(m, x)
            if r <= k:
                s = m + 1
            else:
                e = m - 1
        return e


check()

true, false, null = True, False, None
import aatest_helper

cases = [
    (9, 1, 6),
    (7, 2, 9),
]

aatest_helper.run_test_cases(Solution().findMaximumNumber, cases)

if __name__ == '__main__':
    pass
