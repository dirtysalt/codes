#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        t = 0
        for x in nums:
            t = t ^ x

        exp = (1 << maximumBit) - 1
        for x in reversed(nums):
            ans.append(exp ^ t)
            t = t ^ x
        return ans

cases = [
    ( [0,1,1,3], 2, [0,3,2,3]),
    ([2,3,4,7], 3, [5,2,6,5]),
    ([0,1,2,2,5,7], 3,[4,3,6,4,6,7]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getMaximumXor, cases)




if __name__ == '__main__':
    pass
