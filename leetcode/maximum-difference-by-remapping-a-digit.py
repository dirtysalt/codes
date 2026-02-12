#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minMaxDifference(self, num: int) -> int:
        def test(s, x, y):
            s = s.replace(x, y)
            return int(s)

        s = str(num)
        MAX, MIN = num, num
        for i in range(10):
            a = test(s, str(i), '9')
            b = test(s, str(i), '0')
            MAX = max(MAX, a)
            MIN = min(MIN, b)
        return MAX - MIN


if __name__ == '__main__':
    pass
