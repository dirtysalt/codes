#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 100
        for x in nums1:
            for y in nums2:
                if x == y:
                    r = x
                else:
                    r = min(x, y) * 10 + max(x, y)
                ans = min(ans, r)
        return ans


if __name__ == '__main__':
    pass
