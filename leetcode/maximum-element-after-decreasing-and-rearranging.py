#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        n = len(arr)
        for i in range(1, n):
            most = arr[i-1] + 1
            arr[i] = min(most, arr[i])
        return arr[-1]

if __name__ == '__main__':
    pass
