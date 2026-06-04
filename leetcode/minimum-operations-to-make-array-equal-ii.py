#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            return -1
        n = len(nums1)
        buf, ans = 0, 0
        for i in range(n):
            d = nums2[i] - nums1[i]
            if d % k != 0: return -1
            d = d // k
            if d > 0:
                ans += d
            buf += d
        if buf != 0: return -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 3, 1, 4], [1, 3, 7, 1], 3, 2),
    ([3, 8, 5, 2], [2, 4, 1, 6], 1, -1),
    ([10, 5, 15, 20], [20, 10, 15, 5], 0, -1)
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
