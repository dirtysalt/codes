#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pos = [(x, i) for (i, x) in enumerate(nums)]
        pos.sort(key=lambda x: x[0])

        n = len(nums)
        i = 0
        ans = [0] * n
        while i < n:
            j = i + 1
            while j < n and pos[j][0] - pos[j - 1][0] <= limit:
                j += 1
            # use values as pos[i..j][0]
            # but positions as pos[i..j][1]
            vs = [x[0] for x in pos[i:j]]
            ps = [x[1] for x in pos[i:j]]
            ps.sort()
            for v, p in zip(vs, ps):
                ans[p] = v

            i = j
        return ans


if __name__ == '__main__':
    pass
