#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        ans = [0] * n
        nums.sort()
        mid = (n + 1) // 2
        k = 0
        for i in reversed(range(mid)):
            ans[k] = nums[i]
            k += 2

        k = 1
        for i in reversed(range(mid, n)):
            ans[k] = nums[i]
            k += 2
        nums[:] = ans


cases = [
    [1, 5, 1, 1, 6, 4],
    [1, 5, 1, 1, 6],
    [4, 5, 5, 6]
]
sol = Solution()
for x in cases:
    sol.wiggleSort(x)
    print(x)
