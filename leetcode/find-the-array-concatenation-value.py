#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            if len(nums) == 1:
                ans += nums[0]
                break
            else:
                a, b = nums[0], nums[-1]
                a, b = str(a), str(b)
                c = int(a + b)
                ans += c
                nums = nums[1:-1]
        return ans


if __name__ == '__main__':
    pass
