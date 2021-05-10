#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        cnt = Counter()
        for (b, d) in logs:
            for i in range(b, d):
                cnt[i] += 1

        maxp = max(cnt.values())
        ans = 10000
        for k, v in cnt.items():
            if v == maxp:
                if k < ans:
                    ans = k
        return ans


if __name__ == '__main__':
    pass
