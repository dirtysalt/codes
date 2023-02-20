#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [0] * (2 ** len(primes))
        dp[0] = 1

        def isSpecial(x):
            for p in primes:
                if x % p == 0:
                    c = 0
                    while x % p == 0:
                        x = x // p
                        c += 1
                    if c >= 2: return True
            return False

        tmp = []
        ONE = 0
        for x in nums:
            if x == 1:
                ONE += 1
            elif isSpecial(x):
                continue
            else:
                tmp.append(x)
        nums = tmp

        MOD = 10 ** 9 + 7
        for x in nums:
            ok = True
            bits = []
            st = 0
            for idx, p in enumerate(primes):
                if x % p == 0:
                    x = x // p
                    bits.append(idx)
                    st = st | (1 << idx)

            for j in reversed(range(len(dp))):
                match = True
                for b in bits:
                    if j & (1 << b):
                        match = False
                        break
                if match:
                    dp[j | st] = (dp[j | st] + dp[j]) % MOD

        def pow(a, b):
            s = 1
            while b:
                if b & 0x1:
                    s = s * a
                    s = s % MOD
                b = b // 2
                a = (a * a) % MOD
            return s

        S = pow(2, ONE)
        ans = sum(dp[1:])
        if ans == 0:
            ans = (S - 1)
        elif ONE == 0:
            pass
        else:
            ans = (ans + 1) * S - 1
        ans = ans % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 4, 4, 5], 3),
    ([1], 1),
    ([6, 6], 2),
    ([26, 6, 6, 18], 3),
    ([26, 6, 4, 27, 6, 18], 3),
    ([17, 27, 20, 1, 19], 7),
    ([1, 2, 6, 15, 7, 19, 6, 29, 28, 24, 21, 25, 25, 18, 9, 6, 20, 21, 8, 24, 14, 19, 24, 28, 30, 27, 13, 21, 1, 23, 13,
      29, 24, 29, 18, 7], 9215),
]

aatest_helper.run_test_cases(Solution().squareFreeSubsets, cases)

if __name__ == '__main__':
    pass
