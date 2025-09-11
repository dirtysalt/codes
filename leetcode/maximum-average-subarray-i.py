#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        n = len(nums)
        acc = sum(nums[:k])
        ans = acc
        for i in range(k, n):
            acc += nums[i] - nums[i - k]
            ans = max(acc, ans)
        return ans / k


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
