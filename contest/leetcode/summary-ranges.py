#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        n = len(nums)
        if n == 0: return []

        l, r = nums[0], nums[0]
        ans = []
        for i in range(1, n):
            if (nums[i] - r) != 1:
                ans.append((l, r))
                l, r = nums[i], nums[i]
            else:
                r += 1
        ans.append((l, r))

        ans = ['{}'.format(l) if l == r else '{}->{}'.format(l, r) for l, r in ans]
        return ans
