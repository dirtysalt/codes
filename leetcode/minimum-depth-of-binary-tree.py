#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root: return 0
        if not root and not root.right: return 1
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        ld = self.minDepth(root.left)
        rd = self.minDepth(root.right)
        return min(ld, rd) + 1
