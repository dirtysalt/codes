#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        ts = []
        n = len(dist)
        for i in range(n):
            d = dist[i]
            s = speed[i]
            ts.append((d + s - 1) // s)

        ts.sort()

        ans = n
        for i in range(n):
            if ts[i] <= i:
                ans = i
                break
        return ans

if __name__ == '__main__':
    pass
