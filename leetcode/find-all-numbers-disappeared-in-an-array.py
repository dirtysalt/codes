#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        for i in range(n):
            while nums[i] != (i + 1):
                x = nums[i]
                y = nums[x - 1]
                if y == x:
                    break
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
        ans = []
        for i in range(n):
            if nums[i] != (i + 1):
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
