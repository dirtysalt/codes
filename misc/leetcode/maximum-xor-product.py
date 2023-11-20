#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7

        pa = a >> n
        pb = b >> n
        ans = 0
        for i in reversed(range(n)):
            ca = (a >> i) & 0x1
            cb = (b >> i) & 0x1
            bit = 0
            if ca == cb == 0:
                bit = 1
            elif ca == cb == 1:
                pass
            else:
                if pa >= pb:
                    # preserve pa
                    bit = (1 - cb)
                else:
                    bit = (1 - ca)
            # print((pa, pb), ca, cb, bit)
            ans = (bit << i) | ans
            pa = (pa << 1) | (ca ^ bit)
            pb = (pb << 1) | (cb ^ bit)

        return ((ans ^ a) * (ans ^ b)) % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    (12, 5, 4, 98),
    (6, 7, 5, 930),
    (1, 6, 3, 12),
    (0, 7, 2, 12),
]

aatest_helper.run_test_cases(Solution().maximumXorProduct, cases)

if __name__ == '__main__':
    pass
