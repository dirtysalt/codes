#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for st in range(1 << n):
            t = 0
            for i in range(n):
                if st & (1 << i):
                    t ^= nums[i]
            ans += t

        return ans


if __name__ == '__main__':
    pass
