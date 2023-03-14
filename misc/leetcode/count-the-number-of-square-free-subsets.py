#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [0] * (1 << len(primes))
        dp[0] = 1

        def hasSquareFactor(x):
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
            elif hasSquareFactor(x):
                continue
            else:
                tmp.append(x)
        nums = tmp

        MOD = 10 ** 9 + 7
        for x in nums:
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
        ans = (ans + 1) * S - 1
        ans = ans % MOD
        return ans

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        M = 1 << len(primes)
        mask = [0] * 31

        # preprocess.
        for x in range(1, 31):
            for idx, p in enumerate(primes):
                if x % p == 0:
                    if (x // p) % p == 0:
                        mask[x] = -1
                    else:
                        mask[x] |= (1 << idx)

        MOD = 10 ** 9 + 7
        dp = [0] * M
        dp[0] = 1
        for x in nums:
            m = mask[x]
            if m >= 0:  # mask[1] = 0
                for st in reversed(range(M)):
                    if (st | m) == st:
                        # 选择st, 不选择m. 或者是选择st ^ m, 选择m.
                        dp[st] = (dp[st] + dp[st ^ m]) % MOD

        return (sum(dp) - 1) % MOD

true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 4, 4, 5], 3,),
    ([1], 1),
]

aatest_helper.run_test_cases(Solution().squareFreeSubsets, cases)
