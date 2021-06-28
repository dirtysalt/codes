#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for skip in range(len(nums)):
            def at(i):
                if i < skip:
                    return nums[i]
                else:
                    return nums[i + 1]

            ok = True
            for i in range(1, len(nums) - 1):
                if at(i) <= at(i - 1):
                    ok = False
                    break

            if ok: return True
        return False


true, false, null = True, False, None
cases = [
    ([1, 2, 10, 5, 7], true),
    ([2, 3, 1, 2], false),
    ([1, 1, 1], false),
    ([1, 2, 3], true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canBeIncreasing, cases)

if __name__ == '__main__':
    pass
