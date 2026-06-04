#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        acc = 0
        n = len(coins)
        for i in range(n):
            if (acc + 1) >= coins[i]:
                acc += coins[i]
            else:
                break
        return acc + 1

cases = [
    ([1,3], 2),
    ([1,1,1,4], 8),
    ([1,4,10,3,1], 20),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getMaximumConsecutive, cases)



if __name__ == '__main__':
    pass
