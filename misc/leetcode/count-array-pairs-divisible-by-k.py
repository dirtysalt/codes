#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def primes(N):
    N = int(N ** 0.5)
    P = [1] * (N + 1)
    for i in range(2, N + 1):
        if P[i] == 0: continue
        for j in range(2, N + 1):
            if i * j > N: break
            P[i * j] = 0
    PS = []
    for i in range(2, N + 1):
        if P[i] == 1:
            PS.append(i)
    return PS


def decompose(PS, value):
    factors = []
    for x in PS:
        if value == 1:
            break

        if value % x == 0:
            cnt = 0
            while value % x == 0:
                cnt += 1
                value = value // x
            factors.append((x, cnt))
    if value != 1:
        factors.append((value, 1))
    return factors


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        search = {}
        for x in nums:
            if x % k == 0: continue
            g = gcd(x, k)
            exp = k // g
            search[exp] = 0

        for x in nums:
            for exp in search.keys():
                if x % exp == 0:
                    search[exp] += 1

        ans = 0
        for x in nums:
            if x % k == 0:
                ans += len(nums) - 1
                continue

            if (x * x) % k == 0:
                ans -= 1
            g = gcd(x, k)
            exp = k // g
            ans += search[exp]

        ans = ans // 2
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4, 5], 2, 7),
    ([1, 2, 3, 4], 5, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPairs, cases)

if __name__ == '__main__':
    pass
