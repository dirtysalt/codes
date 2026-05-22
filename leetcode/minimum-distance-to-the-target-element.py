#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 1 << 30

        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))

        return ans

if __name__ == '__main__':
    pass
