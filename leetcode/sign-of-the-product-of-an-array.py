#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                sign = -sign
        return sign

if __name__ == '__main__':
    pass
