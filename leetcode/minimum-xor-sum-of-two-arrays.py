#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        inf = 1 << 30
        dp = [inf] * (1 << n)
        dp[0] = 0

        for st in range(1 << n):
            cs = []
            for i in range(n):
                if (st >> i) & 0x1 == 0:
                    cs.append(i)
            idx = n - len(cs)
            for c in cs:
                v = nums2[c] ^ nums1[idx]
                st2 = st | (1 << c)
                dp[st2] = min(dp[st2], dp[st] + v)

        return dp[-1]


if __name__ == '__main__':
    pass
