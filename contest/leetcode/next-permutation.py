#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = None
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j] and \
                        (k is None or nums[j] < nums[k]):
                    k = j
            if k is not None:
                (nums[i], nums[k]) = (nums[k], nums[i])
                nums[i + 1:] = sorted(nums[i + 1:])
                break
        if k is None: nums.sort()
        # return nums


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1, 2, 3]))
    print(s.nextPermutation([3, 2, 1]))
    print(s.nextPermutation([1, 1, 5]))
    print(s.nextPermutation([1, 1, 5, 4, 0, 4]))
