#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0
        for c in coins:
            ans += (c + 1) // 2
        return ans

cases = [
    ([4,2,1], 4),
    ([2,3,10], 8),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minCount, cases)

if __name__ == '__main__':
    pass
