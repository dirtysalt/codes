#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:


        def find(nums, k):
            n = len(nums)
            j = k
            value = nums[k]
            ans = -1
            # print(nums, k, value)
            for i in reversed(range(k+1)):
                value = min(value, nums[i])
                while (j+1) < n and nums[j+1] >= value: j += 1
                res = value * (j - i + 1)
                # print(i, j, value, res)
                ans = max(ans, res)
            return ans


        a = find(nums, k)
        b = find(nums[::-1], len(nums) - 1 -k)
        return max(a, b)


import aatest_helper

cases = [
    ([1,4,3,7,4,5], 3, 15),
    ([5,5,4,5,4,1,1,1], 0, 20),
]

aatest_helper.run_test_cases(Solution().maximumScore, cases)


if __name__ == '__main__':
    pass
