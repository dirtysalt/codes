#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import Counter
        cnt = Counter()
        for x, y in nums1:
            cnt[x] += y
        for x, y in nums2:
            cnt[x] += y
        keys = list(cnt.keys())
        keys.sort()
        ans = []
        for k in keys:
            ans.append([k, cnt[k]])
        return ans


if __name__ == '__main__':
    pass
