#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        MOD = 1337

        table = [0] * 10
        res = 1
        for i in range(10):
            table[i] = res
            res = (res * a) % MOD

        def pow10(x):
            res = 1
            for _ in range(10):
                res = (res * x) % MOD
            return res

        res = 1
        for p in b:
            res = pow10(res) * table[p]
            res = res % MOD
        return res
