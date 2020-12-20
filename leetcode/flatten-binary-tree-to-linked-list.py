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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def f(root):
            if not root.left and not root.right: return (root, root)
            if not root.left:
                (x, y) = f(root.right)
                root.left = None
                root.right = x
                return (root, y)
            if not root.right:
                (x, y) = f(root.left)
                root.left = None
                root.right = x
                return (root, y)
            (lx, ly) = f(root.left)
            (rx, ry) = f(root.right)
            ly.left = None
            ly.right = rx
            root.left = None
            root.right = lx
            return (root, ry)

        if root:
            f(root)
