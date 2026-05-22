#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def findMaxCI(self, nums: List[int]) -> int:
#         dp = []

#         for x in nums:
#             s, e = 0, len(dp) - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if dp[m] < x:
#                     s = m + 1
#                 else:
#                     e = m - 1

#             # update s
#             if s == len(dp):
#                 dp.append(x)
#             else:
#                 dp[s] = min(dp[s], x)

#         # print(dp)
#         return len(dp)


class Solution:
    def findMaxCI(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] > nums[j - 1]:
                j += 1
            t = (j - i)
            ans = max(ans, t)
            i = j
        return ans


if __name__ == '__main__':
    pass
