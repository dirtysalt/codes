#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 非常巧妙的解法，不断地swap直到element在正确的位置上

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        for i in range(n):
            x = nums[i]
            while 0 < x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
                x = nums[i]

        print(nums)
        for i in range(n):
            x = nums[i]
            if (i + 1) != x:
                return i + 1
        return n + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))
    print(s.firstMissingPositive([3, 4, 1, -1]))
    print(s.firstMissingPositive([1, 1000]))
    print(s.firstMissingPositive([1, 2, 1000]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([3, 4, 0, 2]))
