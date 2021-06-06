#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        f0 = [0] * (n+1)
        f1 = [0] * (n+1)
        f = [f0, f1]

        c0 = 0
        c1 = 1
        for i in range(n):
            c = int(s[i])
            if c != c0:
                f0[i+1] = 1
            if c != c1:
                f1[i+1] = 1
            f0[i+1] += f0[i]
            f1[i+1] += f1[i]
            c0 = 1 - c0
            c1 = 1 - c1

        def changeA(i, j, c):
            ic = (c + i) % 2
            return f[ic][j+1] - f[ic][i]

        ans = n
        for i in range(n):
            exp = (n-i) % 2
            a = changeA(i, n-1, 0) + changeA(0, i-1, exp)
            b = changeA(i, n-1, 1) + changeA(0, i-1, (exp + 1) % 2)
            res = min(a, b)
            ans = min(res, ans)

        return ans

cases = [
    ("111000",2),
    ("010", 0),
    ("1110", 1),
    ("10001100101000000", 5),
    ("01001001101", 2),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minFlips, cases)


if __name__ == '__main__':
    pass
