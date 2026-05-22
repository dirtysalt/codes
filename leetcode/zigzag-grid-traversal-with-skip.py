#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])

        def visit():
            r, c = 0, 0
            d = 1
            while r < n:
                yield r, c
                if (c + d) >= m or (c + d) < 0:
                    d = -d
                    r += 1
                else:
                    c += d

        idx = 0
        ans = []
        for r, c in visit():
            if idx % 2 == 0:
                ans.append(grid[r][c])
            idx += 1
        return ans


if __name__ == '__main__':
    pass
