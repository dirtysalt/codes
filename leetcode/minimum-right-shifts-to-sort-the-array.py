#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        def is_sorted(x):
            return x == sorted(x)

        if is_sorted(nums): return 0

        tmp = nums + nums
        n = len(nums)
        for i in reversed(range(1, n)):
            if is_sorted(tmp[i:i + n]):
                return n - i
        return -1


if __name__ == '__main__':
    pass
