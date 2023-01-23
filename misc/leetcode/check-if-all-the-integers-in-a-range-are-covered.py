#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for p in range(left, right + 1):
            ok = False
            for x, y in ranges:
                if p >= x and p <= y:
                    ok = True
                    break
            if not ok:
                return False
        return True


if __name__ == '__main__':
    pass
