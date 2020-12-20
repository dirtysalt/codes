#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 3
        n = len(nums)
        maxs = [None] * k
        for i in range(n):
            x = nums[i]
            for j in range(k):
                if x is None or x == maxs[j]:
                    break
                elif maxs[j] is None or x > maxs[j]:
                    maxs[j], x = x, maxs[j]

        if maxs[k - 1] is None:
            return maxs[0]
        return maxs[k - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.thirdMax([1, 2]))
    print(sol.thirdMax([1, 2, 3]))
    print(sol.thirdMax([1, 2, 3, 4]))
    print(sol.thirdMax([1, 2, 2, 3]))
