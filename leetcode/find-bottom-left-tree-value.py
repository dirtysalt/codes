#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def visit(node, depth):
            v = node.val
            d = depth

            if node.left:
                v0, d0 = visit(node.left, depth + 1)
                if d0 >= d:
                    v = v0
                    d = d0

            if node.right:
                v1, d1 = visit(node.right, depth + 1)
                if d1 > d:
                    v = v1
                    d = d1

            return v, d

        res, _ = visit(root, depth=0)
        return res
