#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:

        def run(X, Y):
            n = len(Y)
            base = sum(Y)

            acc = [0] * (n + 1)
            for i in range(n):
                acc[i + 1] = acc[i] + X[i] - Y[i]

            l = 0
            ans = 0
            for i in range(1, n + 1):
                if acc[i] < acc[l]:
                    l = i
                value = acc[i] - acc[l]
                ans = max(ans, value)

            return ans + base

        A = run(nums1, nums2)
        B = run(nums2, nums1)
        return max(A, B)


true, false, null = True, False, None
cases = [
    ([60, 60, 60], [10, 90, 10], 210),
    ([20, 40, 20, 70, 30], [50, 20, 50, 40, 20], 220),
    ([7, 11, 13], [1, 1, 1], 31),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumsSplicedArray, cases)

if __name__ == '__main__':
    pass
