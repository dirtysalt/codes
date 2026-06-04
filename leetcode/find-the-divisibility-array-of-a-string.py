#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        p = 0
        for c in word:
            p = p * 10 + ord(c) - ord('0')
            p = p % m
            ans.append(1 if p == 0 else 0)
        return ans


if __name__ == '__main__':
    pass
