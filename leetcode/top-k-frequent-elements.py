#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import heapq
from collections import defaultdict


class Item:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __lt__(self, other):
        if self.v > other.v:
            return True
        if self.v == other.v and self.k < other.k:
            return True
        return False


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = defaultdict(int)
        for v in nums:
            counter[v] += 1
        items = [Item(k, v) for (k, v) in counter.items()]
        res = heapq.nsmallest(k, items)
        res = [x.k for x in res]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1, 1, 2, 2, 3], 2))
