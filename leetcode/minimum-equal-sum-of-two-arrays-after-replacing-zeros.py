#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a, c1 = 0, 0
        for x in nums1:
            if x == 0:
                c1 += 1
                a += 1
            else:
                a += x
        b, c2 = 0, 0
        for x in nums2:
            if x == 0:
                c2 += 1
                b += 1
            else:
                b += x

        if a == b: return a
        if a > b:
            if c2 > 0: return a
            return -1
        else:
            if c1 > 0: return b
            return -1


if __name__ == '__main__':
    pass
