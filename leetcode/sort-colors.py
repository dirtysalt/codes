#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        x, y = 0, n - 1
        i = 0
        while i <= y:
            if nums[i] == 0:
                nums[x], nums[i] = nums[i], nums[x]
                assert nums[x] in (0, 1)
                x += 1
                i += 1
            elif nums[i] == 2:
                nums[y], nums[i] = nums[i], nums[y]
                y -= 1
            else:
                i += 1


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    sol.sortColors(nums)
    print(nums)

    nums = [1, 2, 0]
    sol.sortColors(nums)
    print(nums)
