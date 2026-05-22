#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ws = set(words)
        ans = 0
        for w in words:
            w2 = w[::-1]
            if w == w2: continue
            if w2 in ws:
                ans += 1
        return ans // 2


if __name__ == '__main__':
    pass
