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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        res = []

        def fx(root):
            if not root.left and not root.right:
                res.append(root.val)
                return
            if root.left:
                root.left.val += root.val * 10
                fx(root.left)
            if root.right:
                root.right.val += root.val * 10
                fx(root.right)

        fx(root)
        return sum(res)
