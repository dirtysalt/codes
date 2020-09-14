#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = self.bs(nums, target, eqf='backward')
        if a == -1: return [-1, -1]
        b = self.bs(nums, target, eqf='forward')
        return [a, b]

    def bs(self, nums, target, eqf='forward'):
        (s, e) = (0, len(nums) - 1)
        while s <= e:
            m = (s + e) / 2
            if nums[m] == target:
                if eqf == 'forward' and (m + 1) < len(nums) and nums[m + 1] == target:
                    s = m + 1
                elif eqf == 'backward' and (m - 1) >= 0 and nums[m - 1] == target:
                    e = m - 1
                else:
                    return m
            elif nums[m] > target:
                e = m - 1
            else:
                s = m + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
