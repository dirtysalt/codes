#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        z = 0
        ans = 0
        for x in rungs:
            ans += (x - z - 1) // dist
            z = x
        return ans


if __name__ == '__main__':
    pass
