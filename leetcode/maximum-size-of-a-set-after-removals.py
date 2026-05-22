#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        ss1, ss2 = set(nums1), set(nums2)
        n = len(nums1)
        n2 = n // 2

        a = min(n2, len(ss1 - ss2))
        b = min(n2, len(ss2 - ss1))

        ss = ss1 & ss2
        c = len(ss)
        aa = min(c, n2 - a)
        c -= aa
        bb = min(c, n2 - b)
        c -= bb

        ans = (a + b + aa + bb)
        return ans


if __name__ == '__main__':
    pass
