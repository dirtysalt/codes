#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                sz = (i - j)
                ans += (sz + 1) * sz // 2
                j = i

        sz = len(nums) - j
        ans += (sz + 1) * sz // 2
        return ans


if __name__ == '__main__':
    pass
