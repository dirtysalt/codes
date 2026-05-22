#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(nums1)

        ans = []
        for x in nums2:
            if c[x]:
                ans.append(x)
                c[x] -= 1
        return ans
