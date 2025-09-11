#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# ans = sum(S[0..n-1]), S[i+1] = (2^(i+1) - 1) * (A[i+1]-A[i]) + 2*S[i]

class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        A.sort()
        ans = 0
        last = 0
        p2 = 1
        MOD = 10 ** 9 + 7
        for i in range(n - 1):
            p2 = (p2 * 2) % MOD
            now = (p2 - 1) * (A[i + 1] - A[i]) + 2 * last
            now = now % MOD
            ans = (ans + now) % MOD
            last = now
        return ans
