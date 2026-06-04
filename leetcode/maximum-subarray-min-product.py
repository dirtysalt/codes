#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left = [-1] * n
        right = [-1] * n
        left[0] = 0
        right[-1] = n - 1

        for i in range(1, n):
            x = nums[i]
            j = i - 1
            while j >= 0 and x <= nums[j]:
                j = left[j] - 1
            left[i] = j + 1

        for i in reversed(range(n - 1)):
            x = nums[i]
            j = i + 1
            while j < n and x <= nums[j]:
                j = right[j] + 1
            right[i] = j - 1

        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = nums[i]
        for i in range(n):
            acc[i + 1] += acc[i]

        ans = 0
        for i in range(n):
            l, r = left[i], right[i]
            x = nums[i]
            acc2 = acc[r + 1] - acc[l]
            m = x * acc2
            ans = max(ans, m)
            # print(m)

        MOD = 10 ** 9 + 7
        return ans % MOD


cases = [
    ([1, 2, 3, 2], 14),
    ([2, 3, 3, 1, 2], 18),
    ([3, 1, 5, 6, 4, 2], 60),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSumMinProduct, cases)

if __name__ == '__main__':
    pass
