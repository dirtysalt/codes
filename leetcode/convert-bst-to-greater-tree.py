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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def walk(root, base):
            rsum = walk(root.right, base) if root.right else base
            root.val += rsum
            return walk(root.left, root.val) if root.left else root.val

        if root is None:
            return None
        walk(root, 0)
        return root
