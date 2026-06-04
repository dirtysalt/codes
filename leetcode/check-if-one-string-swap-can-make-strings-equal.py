#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        n =len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)

        if len(diff) > 2 or len(diff) == 1: return False
        if len(diff) == 0: return True

        a, b = diff
        if s1[a] == s2[b] and s1[b] == s2[a]:
            return True
        return False

if __name__ == '__main__':
    pass
