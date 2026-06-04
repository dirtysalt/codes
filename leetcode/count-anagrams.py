#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        Fac = [0] * (len(s) + 1)
        Fac[0] = 1
        for i in range(1, len(Fac)):
            Fac[i] = (Fac[i - 1] * i) % MOD

        def Pow(a, b):
            ans = 1
            while b:
                if b & 0x1:
                    ans = (ans * a) % MOD
                a = (a * a) % MOD
                b = b >> 1
            return ans

        ans = 1
        for s in s.split():
            n = len(s)
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            a = Fac[n]
            b = 1
            for i in range(26):
                b *= Fac[cnt[i]]
                b = b % MOD

            c = (a * Pow(b, MOD - 2)) % MOD
            ans = (ans * c) % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("too hot", 18),
    ("aa", 1),
]

aatest_helper.run_test_cases(Solution().countAnagrams, cases)

if __name__ == '__main__':
    pass
