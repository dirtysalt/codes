#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                nums[i - 1] *= 2
                nums[i] = 0
        ans = []
        for x in nums:
            if x != 0:
                ans.append(x)
        ans = ans + [0] * (n - len(ans))
        return ans


if __name__ == '__main__':
    pass
