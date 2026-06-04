#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        _, val = self.find(root, k)
        return val

    def find(self, root, k):
        # return 1. # of nodes in root 
        # 2. if kth value in root, return value, else None

        if root is None:
            return 0, None

        count, val = self.find(root.left, k)
        if val is not None:
            return 0, val
        if (count + 1) == k:
            return 0, root.val
        count2, val = self.find(root.right, k - count - 1)
        if val is not None:
            return 0, val
        return count + count2 + 1, None
