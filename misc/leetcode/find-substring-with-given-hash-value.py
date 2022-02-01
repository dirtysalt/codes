#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord('a') + 1

        def POW(p, x, m):
            ans = 1
            while x:
                if x & 0x1:
                    ans *= p
                    ans = ans % m
                p = (p * p) % m
                x = x >> 1
            return ans

        PX = POW(power, k - 1, modulo)

        s = s[::-1]
        i, h = 0, 0
        for j in range(k):
            h = h * power + val(s[j])
            h = h % modulo

        index = -1
        while True:
            if h == hashValue:
                index = i
            if (i + k) >= len(s):
                break

            h = (h - val(s[i]) * PX)
            if h < 0:
                z = -h // modulo + 1
                h += z * modulo
            h = (h * power + val(s[i + k])) % modulo
            i += 1

        return s[index:index + k][::-1]


true, false, null = True, False, None
cases = [
    ("leetcode", 7, 20, 2, 0, "ee"),
    ("fbxzaad", 31, 100, 3, 32, "fbx"),
    ("xmmhdakfursinye", 96, 45, 15, 21, "xmmhdakfursinye")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().subStrHash, cases)

if __name__ == '__main__':
    pass
