#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        buf = [1] * n
        idx = 0
        for _ in range(n-1):
            k2 = k
            while k2:
                while buf[idx] == 0:
                    idx = (idx + 1) % n
                idx = (idx + 1) % n
                k2 -= 1
            idx = (idx - 1 + n) % n
            buf[idx] = 0

        for i in range(n):
            if buf[i] == 1:
                return (i+1)
        return -1

cases = [
    (5, 2, 3),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().findTheWinner, cases)


if __name__ == '__main__':
    pass
