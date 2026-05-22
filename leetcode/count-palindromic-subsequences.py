#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countPalindromes(self, s: str) -> int:
        def precompute(s):
            n = len(s)

            # single digit
            SINGLE = [[0] * 10 for _ in range(n)]
            for i in range(n):
                d = ord(s[i]) - ord('0')
                SINGLE[i][d] += 1
                if i > 0:
                    for j in range(10):
                        SINGLE[i][j] += SINGLE[i - 1][j]

            # double digits
            DOUBLE = [[0] * 100 for _ in range(n)]
            for i in range(1, n):
                d = ord(s[i]) - ord('0')
                for j in range(10):
                    value = d * 10 + j
                    DOUBLE[i][value] += SINGLE[i - 1][j]
                for j in range(100):
                    DOUBLE[i][j] += DOUBLE[i - 1][j]

            return DOUBLE

        n = len(s)
        DA = precompute(s)
        DB = precompute(s[::-1])
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(2, n - 2):
            for j in range(100):
                a = DA[i - 1][j]
                b = DB[n - 1 - (i + 1)][j]
                ans += (a * b)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ("103301", 2),
    ("0000000", 21),
    ("9999900000", 2),
]

aatest_helper.run_test_cases(Solution().countPalindromes, cases)

if __name__ == '__main__':
    pass
