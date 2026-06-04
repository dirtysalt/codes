#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = set(nums1), set(nums2)
        ans = [0, 0]
        for x in nums1:
            if x in b:
                ans[0] += 1
        for x in nums2:
            if x in a:
                ans[1] += 1
        return ans


if __name__ == '__main__':
    pass
