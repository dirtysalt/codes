#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        B0 = [x for x in nums2 if x < 0]
        B1 = [x for x in nums2 if x > 0]
        Z = len([x for x in nums2 if x == 0])

        def search(value):
            res = 0
            B00, B10 = len(B0) - 1, 0
            B01, B11 = 0, len(B1) - 1

            for x in nums1:
                if x == 0:
                    if value >= 0:
                        res += len(nums2)
                    continue

                if value >= 0:
                    res += Z

                if x < 0:
                    while B00 >= 0 and x * B0[B00] <= value:
                        B00 -= 1
                    res += len(B0) - 1 - B00
                    while B10 < len(B1) and x * B1[B10] > value:
                        B10 += 1
                    res += len(B1) - B10
                else:
                    while B01 < len(B0) and x * B0[B01] <= value:
                        B01 += 1
                    res += B01
                    while B11 >= 0 and x * B1[B11] > value:
                        B11 -= 1
                    res += B11 + 1
            return res

        s, e = -(10 ** 10), (10 ** 10)
        while s <= e:
            m = (s + e) // 2
            kth = search(m)
            if kth >= k:
                e = m - 1
            else:
                s = m + 1

        return s


true, false, null = True, False, None
cases = [
    ([2, 5], [3, 4], 2, 8),
    ([-4, -2, 0, 3], [2, 4], 6, 0),
    ([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3, -6),
    ([-8, -6, 0, 1, 4, 10], [-10, -8, -7, -6], 19, 48),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kthSmallestProduct, cases)

if __name__ == '__main__':
    pass
