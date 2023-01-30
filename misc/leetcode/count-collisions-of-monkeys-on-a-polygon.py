#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def pow(a, b):
            r = 1
            while b:
                if b & 0x1:
                    r = (r * a) % MOD
                b = b >> 1
                a = (a * a) % MOD
            return r

        ans = pow(2, n) - 2
        ans = (ans + MOD) % MOD
        return ans


if __name__ == '__main__':
    pass
