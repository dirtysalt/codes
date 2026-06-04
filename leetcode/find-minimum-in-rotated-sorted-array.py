#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        s, e = 0, n - 1
        while s < e:
            if nums[s] < nums[e]:
                return nums[s]
            m = (s + e) // 2
            if nums[m] >= nums[s]:
                s = m + 1
            else:
                e = m
        assert s == e
        return nums[s]


if __name__ == '__main__':
    s = Solution()
    print((s.findMin([3, 4, 5, 1, 2])))
    print((s.findMin([4, 5, 6, 7, 0, 1, 2])))
    print((s.findMin([4, 5])))
    print((s.findMin([3, 1, 2])))
