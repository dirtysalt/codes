#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        from collections import defaultdict
        from sortedcontainers import SortedList
        pos = defaultdict(SortedList)
        acc = 0
        for i in range(n):
            x = nums[i]
            acc += x
            pos[x].add(acc)

        INF = (1 << 63)
        ans = -INF
        acc = 0
        for i in range(n):
            x = nums[i]

            if pos[x + k]:
                r = pos[x + k][-1]
                ans = max(ans, r - acc)

            if pos[x - k]:
                r = pos[x - k][-1]
                ans = max(ans, r - acc)

            acc += x
            pos[x].remove(acc)

        if ans == -INF:
            ans = 0
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 5, 6], 1, 11),
    ([-1, 3, 2, 4, 5], 3, 11),
    ([-1, -2, -3, -4], 2, -6),
]

aatest_helper.run_test_cases(Solution().maximumSubarraySum, cases)

if __name__ == '__main__':
    pass
