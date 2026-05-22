#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums) + 1
        ans = 0
        for x in range(n):
            ans ^= x
        for x in nums:
            ans ^= x
        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.missingNumber([3, 0, 1])))
