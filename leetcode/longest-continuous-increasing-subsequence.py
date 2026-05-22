#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        ans = 0
        j = 0
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                ans = max(ans, i - j)
                j = i
        ans = max(ans, n - j)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLengthOfLCIS([1, 3, 5, 4, 7]))
    print(sol.findLengthOfLCIS([2, 2, 2, 2, 2]))
