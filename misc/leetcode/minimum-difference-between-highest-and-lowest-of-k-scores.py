#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1 << 30
        for j in range(k - 1, len(nums)):
            i = j - (k - 1)
            diff = nums[j] - nums[i]
            ans = min(ans, diff)
        return ans


if __name__ == '__main__':
    pass
