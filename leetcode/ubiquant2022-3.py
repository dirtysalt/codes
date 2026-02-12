#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, numbers: List[int]) -> int:
        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        r = 1
        for x in numbers:
            r = lcm(r, x)

        ans = 0
        for x in numbers:
            rem = r // x
            t = 0
            while rem % 2 == 0:
                rem = rem // 2
                t += 1
            while rem % 3 == 0:
                rem = rem // 3
                t += 1
            if rem != 1: return -1
            ans += t
        return ans


if __name__ == '__main__':
    pass
