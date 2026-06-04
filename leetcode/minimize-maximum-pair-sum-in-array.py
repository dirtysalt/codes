#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n // 2):
            x = nums[i] + nums[n - 1 - i]
            ans = max(ans, x)
        return ans


if __name__ == '__main__':
    pass
