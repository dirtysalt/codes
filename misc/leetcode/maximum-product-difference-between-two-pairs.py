#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        a, b = nums[-1], nums[-2]
        c, d = nums[0], nums[1]

        return (a * b) - (c * d)


if __name__ == '__main__':
    pass
