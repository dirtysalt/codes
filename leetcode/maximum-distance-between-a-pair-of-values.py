#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = 0
        ans = 0
        for i in range(len(nums1)):
            x = nums1[i]
            while j < len(nums2) and nums2[j] >= x:
                j += 1
            if (j - 1) < len(nums2) and nums2[j - 1] >= x:
                dist = j - 1 - i
                ans = max(ans, dist)
        return ans


if __name__ == '__main__':
    pass
