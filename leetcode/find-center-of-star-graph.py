#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        e = [0] * (n+1)

        for x, y in edges:
            e[x] += 1
            e[y] += 1

        for i in range(1, n+1):
            if e[i] == (n-1):
                return i

        return -1



if __name__ == '__main__':
    pass
