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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def f(root):
            if not root: return (True, 0)
            (lok, ld) = f(root.left)
            (rok, rd) = f(root.right)
            if not lok or not rok or abs(ld - rd) > 1:
                return (False, -1)
            return (True, max(ld, rd) + 1)

        (res, _) = f(root)
        return res
