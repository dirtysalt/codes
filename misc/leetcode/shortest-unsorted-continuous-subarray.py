#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这题目的thread里面给的O(1)space, O(n)time的方法非常巧妙
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103057/Java-O(n)-Time-O(1)-Space

# class Solution:
#     def findUnsortedSubarray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         n = len(nums)
#         if n == 0: return 0
#
#         right = [0] * n
#         right[-1] = nums[-1]
#         for i in range(n - 2, -1, -1):
#             right[i] = min(right[i + 1], nums[i])
#         left = [0] * n
#         left[0] = nums[0]
#         for i in range(1, n):
#             left[i] = max(left[i - 1], nums[i])
#
#         x, y = None, None
#         for i in range(n):
#             if not (left[i] <= nums[i] <= right[i]):
#                 x = i
#                 break
#         for i in reversed(range(n)):
#             if not (left[i] <= nums[i] <= right[i]):
#                 y = i
#                 break
#         if x is None:
#             return 0
#         return y - x + 1

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0: return 0

        left_max = nums[0]
        end = None
        for i in range(n):
            left_max = max(left_max, nums[i])
            if nums[i] < left_max:
                end = i

        right_min = nums[-1]
        begin = None
        for i in reversed(range(n)):
            right_min = min(right_min, nums[i])
            if nums[i] > right_min:
                begin = i

        if end is None:
            return 0
        return end - begin + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(sol.findUnsortedSubarray([2, 2, 4, 4, 9, 9, 15]))
    print(sol.findUnsortedSubarray([1, 1, 1]))
    print(sol.findUnsortedSubarray([1]))
    print(sol.findUnsortedSubarray([1, 2, 0, -1]))
