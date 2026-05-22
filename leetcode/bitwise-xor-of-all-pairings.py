#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # n, m
        # x0 will be xored with m times.
        # y0 will be xored with n times.

        n, m = len(nums1), len(nums2)
        ans = 0

        for x in nums1:
            if m % 2 == 1:
                ans ^= x
        for x in nums2:
            if n % 2 == 1:
                ans ^= x
        return ans


if __name__ == '__main__':
    pass
