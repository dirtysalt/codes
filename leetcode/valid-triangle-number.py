#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                # k = bisect.bisect_left(nums, nums[i] + nums[j], j + 1)
                # ans += (k - 1 - j)

                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1

                if k > j:
                    ans += k - j - 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.triangleNumber([2, 2, 3, 4]))
    print(sol.triangleNumber([0, 0, 0]))
