#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        if n == 0:
            return 0

        A.sort()
        MOD = 10 ** 9 + 7

        times = {}
        ans = 0
        for i in range(n):
            x = A[i]
            res = 1
            for j in range(i - 1, -1, -1):
                y = A[j]
                if x % y == 0:
                    z = x // y
                    if z in times:
                        res += (times[y] % MOD) * (times[z] % MOD)
                        res %= MOD
            times[x] = res
            ans = (ans + res) % MOD
        return ans
