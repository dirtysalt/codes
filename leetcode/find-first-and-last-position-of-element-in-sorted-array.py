#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        a = bisect.bisect_left(nums, target)
        b = bisect.bisect_right(nums, target) - 1

        if 0 <= a < n and nums[a] == target:
            pass
        else:
            a = -1

        if 0 <= b < n and nums[b] == target:
            pass
        else:
            b = -1

        return [a, b]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))
