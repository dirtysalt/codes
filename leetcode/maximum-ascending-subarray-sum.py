#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n =len(nums)
        ans = 0
        for i in range(n):
            acc = nums[i]
            for j in range(i+1, n):
                if nums[j] > nums[j-1]:
                    acc += nums[j]
                else:
                    break
            ans = max(ans, acc)
        return ans

if __name__ == '__main__':
    pass
