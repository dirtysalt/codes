#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            x = abs(nums[i] - nums[(i + 1) % len(nums)])
            ans = max(ans, x)
        return ans


if __name__ == '__main__':
    pass
