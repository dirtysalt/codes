#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def cons(nums):
            if not nums:
                return None

            pos = 0
            for i in range(len(nums)):
                if nums[i] > nums[pos]:
                    pos = i

            l = cons(nums[:pos])
            r = cons(nums[pos + 1:])
            t = TreeNode(nums[pos])
            t.left = l
            t.right = r
            return t

        ans = cons(nums)
        return ans
