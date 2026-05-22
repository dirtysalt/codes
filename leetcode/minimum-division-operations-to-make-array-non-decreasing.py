#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        tmp = nums.copy()
        M = max(nums)

        def get_primes(N):
            ps = []
            mask = [0] * (N + 1)
            for i in range(2, N + 1):
                if mask[i] == 1: continue
                for j in range(2, N + 1):
                    if i * j > N: break
                    mask[i * j] = 1
            for i in range(2, N + 1):
                if mask[i] == 0:
                    ps.append(i)
            return ps

        P = get_primes(int(M ** 0.5) + 10)

        @functools.lru_cache(None)
        def factor(x):
            for p in P:
                if x % p == 0:
                    return p
            return x

        ans = 0
        for i in reversed(range(len(tmp) - 1)):
            if tmp[i] > tmp[i + 1]:
                f = factor(tmp[i])
                if f > tmp[i + 1]:
                    return -1
                tmp[i] = f
                ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([25, 7], 1),
    ([7, 7, 6], -1),
    ([1, 1, 1, 1], 0),
    ([9, 2], -1),
    ([288, 7], 1),
    ([78697, 89753, 97789, 155719, 178093, 195977, 208997, 244033, 265163, 287491, 306517, 319483, 340777, 353359,
      429017, 442271, 507713, 515507, 543791, 572461, 597131, 598541, 621031, 632629, 643723, 759881, 871837, 886993,
      914647, 981077], 0),
    ([27, 23], 1),
    ([240, 2, 11], 1),
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
