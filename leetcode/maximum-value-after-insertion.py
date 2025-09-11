#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxValue(self, n: str, x: int) -> str:

        ii = len(n)
        f = 1
        start = 0
        if n[0] == '-':
            f = -1
            start = 1
        if True:
            for i in range(start, len(n)):
                c = int(n[i])
                if c * f < x * f:
                    ii = i
                    break
        ans = n[:ii] + str(x) + n[ii:]
        return ans


if __name__ == '__main__':
    pass
