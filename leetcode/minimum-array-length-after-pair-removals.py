#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        def test(K):
            i, j = 0, K
            while i < K and j < len(nums):
                if nums[j] > nums[i]:
                    i += 1
                j += 1
            return i == K

        s, e = 0, len(nums) // 2
        while s <= e:
            m = (s + e) // 2
            if test(m):
                s = m + 1
            else:
                e = m - 1
        return len(nums) - 2 * e


if __name__ == '__main__':
    pass
