#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s, e = 0, len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            l = nums[m - 1] if m > s else None
            r = nums[m + 1] if m < e else None
            if (l is None or nums[m] > l) and (r is None or nums[m] > r):
                return m
            elif l is not None and nums[m] < l:
                e = m - 1
            else:
                s = m + 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
