#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:

        from functools import cache

        pos = []
        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)
        if not pos: return 0

        MOD = 10 ** 9 + 7

        @cache
        def search(j):
            if j == (len(pos) - 1):
                return 1
            a, b = pos[j], pos[j + 1]
            # from i to pos[j] ... pos[j+1] - 1
            res = (b - a) * search(j + 1) % MOD
            return res

        ans = search(0)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([0, 1, 0, 0, 1], 3,),
    ([0, 1, 0], 1),
    ([0, 0, 1, 1], 1),
]

aatest_helper.run_test_cases(Solution().numberOfGoodSubarraySplits, cases)

if __name__ == '__main__':
    pass
