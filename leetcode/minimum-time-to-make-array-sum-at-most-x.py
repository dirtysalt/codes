#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        xs = list(zip(nums1, nums2))
        xs.sort(key=lambda x: x[1])
        n = len(xs)
        f = [0] * (n + 1)
        f[0] = 0
        for a, b in xs:
            for j in reversed(range(1, n + 1)):
                f[j] = max(f[j], f[j - 1] + a + b * j)

        s1 = sum(nums1)
        s2 = sum(nums2)
        for t in range(n + 1):
            if (s1 + s2 * t - f[t]) <= x:
                return t
        return -1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], [1, 2, 3], 4, 3),
    ([1, 2, 3], [3, 3, 3], 4, -1)
]

aatest_helper.run_test_cases(Solution().minimumTime, cases)

if __name__ == '__main__':
    pass
