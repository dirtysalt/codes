#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        xs = [(nums[i], i) for i in range(len(nums))]
        xs.sort()
        for i in range(1, len(xs)):
            if xs[i][0] == xs[i - 1][0] and (xs[i][1] - xs[i - 1][1]) <= k:
                return True
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = i
            else:
                j = pos[x]
                if (i - j) <= k:
                    return True
                pos[x] = i
        return False
