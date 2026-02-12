#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n:
            ans += n % k
            n = n // k
        return ans

if __name__ == '__main__':
    pass
