#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans, j = 0, 0
        for i in range(n):
            while j < n and nums[j] <= (nums[i] + 2 * k): j += 1
            d = (j - i)
            ans = max(ans, d)
        return ans


if __name__ == '__main__':
    pass
