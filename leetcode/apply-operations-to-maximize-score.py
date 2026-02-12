#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


def compute_primes(N):
    ps = [0] * (N + 1)
    for i in range(2, N + 1):
        if ps[i] == 1: continue
        for j in range(2, N + 1):
            if i * j > N: break
            ps[i * j] = 1
    res = []
    for x in range(2, N + 1):
        if ps[x] == 0:
            res.append(x)
    return res


def compute_factors(nums):
    P = compute_primes(int(max(nums) ** 0.5) + 2)
    values = []

    @functools.cache
    def f(x):
        if x == 1: return 0
        c = 0
        for p in P:
            if x % p == 0:
                c += 1
                while x % p == 0:
                    x = x // p
                if x == 1:
                    break
        if x > 1:
            c += 1
        return c

    for x in nums:
        c = f(x)
        values.append(c)
    return values


def POW(a, b, MOD):
    t = a
    res = 1
    while b:
        if b & 0x1:
            res = res * t
            res %= MOD
        b = b >> 1
        t = t * t
        t = t % MOD
    return res


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        factors = compute_factors(nums)
        n = len(nums)
        L = [-1] * n
        for i in range(1, n):
            j = i - 1
            while j >= 0 and factors[i] > factors[j]:
                j = L[j]
            L[i] = j
        R = [n] * n
        for i in reversed(range(n - 1)):
            j = i + 1
            while j < n and factors[i] >= factors[j]:
                j = R[j]
            R[i] = j

        from collections import Counter
        C = Counter()
        for i in range(n):
            l = i - L[i]
            r = R[i] - i
            x = nums[i]
            C[x] += l * r
        keys = list(C.keys())
        keys.sort(reverse=True)
        MOD = 10 ** 9 + 7
        ans = 1
        for x in keys:
            v = min(C[x], k)
            ans *= POW(x, v, MOD)
            ans = ans % MOD
            k -= v
            if k == 0:
                break
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([8, 3, 9, 3, 8], 2, 81),
    ([19, 12, 14, 6, 10, 18], 3, 4788)
]

cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().maximumScore, cases)

if __name__ == '__main__':
    pass
