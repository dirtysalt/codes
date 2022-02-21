#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [-1] * n
        for i in range(n):
            x = nums2[i]
            pos2[x] = i

        pos1 = [-1] * n
        for i in range(n):
            x = nums1[i]
            p = pos2[x]
            pos1[i] = p

        left = SortedList()
        right = SortedList(pos1)
        ans = 0
        for i in range(n):
            p = pos1[i]
            right.remove(p)
            left.add(p)
            # search how many elements in left is < p
            # and how many elements in right is > p
            a = left.bisect_left(p)
            b = len(right) - right.bisect_right(p)
            ans += a * b
        return ans


true, false, null = True, False, None
cases = [
    ([2, 0, 1, 3], [0, 1, 2, 3], 1),
    ([4, 0, 1, 3, 2], [4, 1, 0, 2, 3], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().goodTriplets, cases)

if __name__ == '__main__':
    pass
