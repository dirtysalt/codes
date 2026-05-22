#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        tt = sum(nums)
        ans = []
        l = 0
        for x in nums:
            r = tt - l - x
            ans.append(abs(l - r))
            l += x
        return ans


if __name__ == '__main__':
    pass
