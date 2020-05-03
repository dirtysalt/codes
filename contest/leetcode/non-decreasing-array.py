#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        fix = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                # 尝试将nums[i]修复为nums[i-1], 确保nums[i-1] <= nums[i+1]
                # 或者是nums[i-1]修复为nums[i], 这样nums[i-2] <= nums[i]
                if (i < 2 or nums[i] >= nums[i - 2]) or \
                        (i > n - 2 or nums[i - 1] <= nums[i + 1]):
                    fix += 1
                    if fix > 1:
                        return False
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkPossibility([4, 2, 3]))
    print(sol.checkPossibility([4, 2, 1]))
    print(sol.checkPossibility([3, 4, 2, 3]))
    print(sol.checkPossibility([-1, 4, 2, 3]))
    print(sol.checkPossibility([2, 3, 3, 2, 4]))
