#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3: return 0
        nums.sort()
        # [a, b, c.., ]
        # -> [c, .... ]
        A = nums[-1] - nums[2]
        # [..., a, b, c]
        # -> [..., a]
        B = nums[-3] - nums[0]
        # [a, b, c, .. y, z]
        # -> [b,.. y]
        C = nums[-2] - nums[1]
        ans = min(A, B, C)
        return ans


if __name__ == '__main__':
    pass
