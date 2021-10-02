#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(nums[j] - nums[i], ans)
        if ans == 0:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
