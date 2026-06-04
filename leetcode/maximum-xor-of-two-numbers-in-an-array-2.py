#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Tree:
    def __init__(self, lgn):
        self.lgn = lgn
        self.base = 1 << lgn
        self.size = 1 << (lgn + 1)
        self.data = [False] * self.size

    def insert(self, x):
        p = 1
        for i in reversed(range(self.lgn)):
            p = 2 * p
            if (x >> i) & 0x1:
                p += 1
            self.data[p] = True

    def query(self, x):
        p = 1
        for i in reversed(range(self.lgn)):
            p = 2 * p
            if (x >> i) & 0x1:
                if self.data[p]:
                    pass
                else:
                    p += 1
            else:
                if self.data[p + 1]:
                    p += 1
                else:
                    pass
        return p - self.base


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxn = max(nums)
        lgn = 1
        while (1 << lgn) <= maxn:
            lgn += 1
        lgn += 1

        tree = Tree(lgn)
        for x in nums:
            tree.insert(x)

        ans = 0
        for x in nums:
            y = tree.query(x)
            ans = max(ans, x ^ y)
        return ans


true, false, null = True, False, None
cases = [
    ([3, 10, 5, 25, 2, 8], 28),
    ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),
    ([8, 10, 2], 10)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findMaximumXOR, cases)

if __name__ == '__main__':
    pass
