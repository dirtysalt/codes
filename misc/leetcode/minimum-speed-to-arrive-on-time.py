#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def test(s):
            t = 0
            for d in dist[:-1]:
                x = d // s
                if d % s != 0:
                    x += 1
                t += x
            t += dist[-1] * 1.0 / s
            if t <= hour:
                return True
            return False

        inf = 10 ** 9
        a, b = 1, inf
        while a <= b:
            s = (a + b) // 2
            if test(s):
                b = s - 1
            else:
                a = s + 1

        ans = a
        if ans > inf:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
