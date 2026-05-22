#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        n = len(nums)
        lt = self.sortedArrayToBST(nums[:n / 2])
        rt = self.sortedArrayToBST(nums[n / 2 + 1:])
        t = TreeNode(nums[n / 2])
        t.left = lt
        t.right = rt
        return t
