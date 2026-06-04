#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        cnt = Counter()
        for x in nums2:
            cnt[x] += 1
        self.cnt = cnt

    def add(self, index: int, val: int) -> None:
        cnt = self.cnt
        x = self.nums2[index]
        cnt[x] -= 1
        x += val
        self.nums2[index] = x
        cnt[x] += 1

    def count(self, tot: int) -> int:
        cnt = self.cnt
        ans = 0
        for x in self.nums1:
            ans += cnt[tot - x]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)


if __name__ == '__main__':
    pass
