#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        ans = 1
        r = nums[0] + nums[1]
        for i in range(2, len(nums) // 2 * 2, 2):
            if nums[i] + nums[i + 1] == r:
                ans += 1
            else:
                break
        return ans


if __name__ == '__main__':
    pass
