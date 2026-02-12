#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        i = 0
        ans = 0
        while i < n:
            if nums[i] == 0:
                i += 1
                continue
            j = i
            while j < n and nums[j] == 1:
                j += 1
            ans = max(j - i, ans)
            i = j
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 0, 1]))
    print(sol.findMaxConsecutiveOnes([0, 0, 0]))
