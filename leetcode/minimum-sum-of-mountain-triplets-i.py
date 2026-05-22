#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [-1] * n
        right = [-1] * n

        from sortedcontainers import SortedList
        sl = SortedList()
        for i in range(1, n - 1):
            sl.add(nums[i - 1])
            left[i] = sl[0]

        sl = SortedList()
        for i in reversed(range(1, n - 1)):
            sl.add(nums[i + 1])
            right[i] = sl[0]

        INF = 1 << 30
        ans = INF
        for i in range(1, n - 1):
            a, b = left[i], right[i]
            if a < nums[i] and b < nums[i]:
                ans = min(ans, a + b + nums[i])
        if ans == INF:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
