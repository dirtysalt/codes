#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def ok(x, i):
            for j in range(len(nums2)):
                while i < len(nums1) and (nums1[i] + x) < nums2[j]:
                    i += 1
                if i == len(nums1) or (nums1[i] + x) > nums2[j]:
                    return False
                i += 1
            return True

        ans = 1 << 30
        for i in range(len(nums1)):
            x = nums2[0] - nums1[i]
            if ok(x, i):
                ans = min(ans, x)
        return ans


if __name__ == '__main__':
    pass
