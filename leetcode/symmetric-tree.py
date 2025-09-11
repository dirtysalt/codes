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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def sym(a, b):
            if not a and not b: return True
            if not a or not b: return False
            if a.val != b.val: return False
            return sym(a.left, b.right) and sym(a.right, b.left)

        return sym(root, root)
