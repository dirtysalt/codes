#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        i, j = 0, mid
        ans = []
        while i < mid or j < n:
            if i < mid:
                ans.append(nums[i])
                i += 1
            if j < n:
                ans.append(nums[j])
                j += 1
        return ans


if __name__ == '__main__':
    pass
