#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        rev = []
        for x in nums:
            t = 0
            while x:
                t = t * 10 + x % 10
                x = x // 10
            rev.append(t)

        from collections import Counter
        cnt = Counter()
        for i in range(len(nums)):
            d = nums[i] - rev[i]
            cnt[d] += 1

        ans = 0
        for v in cnt.values():
            ans += v * (v-1) // 2
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


if __name__ == '__main__':
    pass
