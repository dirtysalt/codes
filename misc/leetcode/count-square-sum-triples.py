#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0

        for c in range(1, n + 1):
            for a in range(1, c):
                b2 = c * c - a * a
                b = int(b2 ** 0.5)
                if b * b == b2:
                    ans += 1

        return ans


if __name__ == '__main__':
    pass
