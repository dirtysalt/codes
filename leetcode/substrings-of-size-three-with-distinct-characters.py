#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            ss = s[i:i + 3]
            if len(set(ss)) == 3:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
