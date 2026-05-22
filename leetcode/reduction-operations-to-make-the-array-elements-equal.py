#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        keys = list(cnt.keys())
        keys.sort(reverse = True)

        ans = 0
        for i in range(1, len(keys)):
            k = keys[i-1]
            ans += cnt[k]
            k2 = keys[i]
            cnt[k2] += cnt[k]

        return ans

if __name__ == '__main__':
    pass
