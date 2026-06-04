#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        base = 1
        while base < k:
            base = base * 2
        inf = -(1 << 30)

        heap = [inf] * (2 * base)

        def adjust(i, v):
            heap[i + base] = v
            p = (i + base) // 2
            while p >= 1:
                heap[p] = max(heap[2 * p], heap[2 * p + 1])
                p = p // 2

        for i in range(k):
            adjust(i, nums[i])

        ans = []
        ans.append(heap[1])
        for i in range(k, len(nums)):
            adjust(i % k, nums[i])
            ans.append(heap[1])

        return ans


cases = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSlidingWindow, cases)
