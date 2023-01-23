#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            while i < j and nums[i] + nums[j] > target: j-=1
            ans += (j - i)
            i += 1
        MOD = 10 ** 9 + 7
        return ans % MOD

if __name__ == '__main__':
    pass
