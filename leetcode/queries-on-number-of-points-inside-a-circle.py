#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        def ok(x0, y0, x1, y1, r):
            a = (x0-x1) ** 2 + (y0 - y1) ** 2
            b = r ** 2
            return a <= b

        for (x1, y1, r) in queries:
            cnt = 0
            for (x0, y0) in points:
                if ok(x0, y0, x1, y1, r):
                    cnt += 1
            ans.append(cnt)
        return ans

if __name__ == '__main__':
    pass
