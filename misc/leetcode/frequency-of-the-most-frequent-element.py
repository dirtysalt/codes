#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        freq = 1
        tail = k
        j = 0
        ans = 1

        for i in range(1, len(nums)):
            d = nums[i] - nums[i-1]
            # 假设freq个nums[i-1]全部升级到nums[i]上
            tail -= freq * d
            while tail < 0 and j < i:
                # 放弃j
                tail += nums[i] - nums[j]
                j += 1
                freq -= 1
            # 考虑nums[i]
            freq += 1
            ans = max(ans, freq)

        return ans

cases = [
    ([1,2,4], 5, 3),
    ([1,4,8,13], 5, 2),
    ([3,9,6], 2, 1),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maxFrequency, cases)


if __name__ == '__main__':
    pass
