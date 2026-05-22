#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = nums[-1]
        for i in range(1, len(nums)):
            r = nums[i] - nums[i - 1]
            ans = min(ans, r)
        return ans


if __name__ == '__main__':
    pass
