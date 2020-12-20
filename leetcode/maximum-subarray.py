#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = -1
        acc = 0
        for n in nums:
            acc += n
            if acc < 0:
                acc = 0
            else:
                ans = max(ans, acc)
        if ans < 0:
            ans = max(nums)
        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.maxSubArray([-1, -2])))
