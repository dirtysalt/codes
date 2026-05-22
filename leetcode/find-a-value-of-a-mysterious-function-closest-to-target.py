#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:

        n = len(arr)

        def getBits(x):
            bits = [0] * 32
            for i in range(32):
                if (x >> i) & 0x1:
                    bits[i] += 1
            return bits

        def addBits(x, y):
            for i in range(32):
                x[i] += y[i]

        def subBits(x, y):
            for i in range(32):
                x[i] -= y[i]

        def cons(bits, size):
            t = 0
            for i in range(32):
                if bits[i] == size:
                    t |= (1 << i)
            return t

        BITS = [0] * 32
        t = arr[0]
        j = 0
        ans = 1 << 30
        for i in range(n):
            x = arr[i]

            t = t & x
            bits = getBits(x)
            addBits(BITS, bits)

            # print(t)
            ans = min(ans, abs(t - target))

            if t < target:
                while j < i and t < target:
                    y = arr[j]
                    bits = getBits(y)
                    subBits(BITS, bits)
                    t = cons(BITS, i - j)
                    # print(t)
                    ans = min(ans, abs(t - target))
                    j += 1

        return ans


cases = [
    ([9, 12, 3, 7, 15], 5, 2),
    ([1000000, 1000000, 1000000], 1, 999999),
    ([1, 2, 4, 8, 16], 0, 0),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().closestToTarget, cases)
