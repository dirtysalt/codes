#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            if nums[i] > threshold or nums[i] % 2 != 0: continue
            c = 1
            for j in range(i + 1, n):
                if nums[j] > threshold: break
                if nums[j] % 2 == nums[j - 1] % 2: break
                c += 1
            ans = max(ans, c)
        return ans


if __name__ == '__main__':
    pass
