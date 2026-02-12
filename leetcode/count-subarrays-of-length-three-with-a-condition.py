#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] % 2 != 0: continue
            x, y = nums[i - 1], nums[i + 1]
            if (x + y) * 2 == nums[i]:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
