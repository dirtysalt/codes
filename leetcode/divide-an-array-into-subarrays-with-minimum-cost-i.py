#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        ans = sum(nums)
        for i in (0,):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    c = nums[i] + nums[j] + nums[k]
                    ans = min(ans, c)
        return ans


if __name__ == '__main__':
    pass
