#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        A = [-1] * n
        for i in range(1, n):
            j = i - 1
            while j >= 0 and nums[i] <= nums[j]:
                j = A[j]
            A[i] = j

        B = [n] * n
        for i in reversed(range(n - 1)):
            j = i + 1
            while j < n and nums[i] <= nums[j]:
                j = B[j]
            B[i] = j

        for i in range(n):
            sz = B[i] - A[i] - 1
            if nums[i] * sz > threshold:
                return sz
        return -1


true, false, null = True, False, None
cases = [
    ([1, 3, 4, 3, 1], 6, 3),
    ([6, 5, 6, 5, 8], 7, 5),
    ([1000000000], 1, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().validSubarraySize, cases)

if __name__ == '__main__':
    pass
