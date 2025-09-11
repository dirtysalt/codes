#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def check(x):
            a, b = 0, 0
            while x:
                x2 = x & (x - 1)
                c = x - x2
                x = x2
                a += 1
                b += c
                # print(x, x2, c, a, b)
            return a, b

        if num2 == 0:
            a, b = check(num1)
            # assert a == b
            return a

        ans = 0
        while num1 > 0:
            a, b = check(num1)
            if a <= ans <= b:
                return ans
            num1 -= num2
            ans += 1
        return -1


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, -2, 3),
    (5, 7, -1),
    (5, 4, 1),
    (1000000000, 0, 13),
]

aatest_helper.run_test_cases(Solution().makeTheIntegerZero, cases)

if __name__ == '__main__':
    pass
