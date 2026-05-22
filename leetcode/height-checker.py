#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # exp = sorted(heights)
        # ans = 0
        # for i in range(len(heights)):
        #     if exp[i] != heights[i]:
        #         ans += 1
        # return ans

        cnt = [0] * 101
        for h in heights:
            cnt[h] += 1

        ans = 0
        idx = 0
        for h in heights:
            while cnt[idx] == 0:
                idx += 1
            if h != idx:
                ans += 1
            cnt[idx] -= 1
        return ans

if __name__ == '__main__':
    pass
