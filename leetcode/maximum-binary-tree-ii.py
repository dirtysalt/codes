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
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:

        def f(root):
            if root is None:
                x = TreeNode(val)
                return x

            if val > root.val:
                x = TreeNode(val)
                x.left = root
                return x

            root.right = f(root.right)
            return root

        root = f(root)
        return root
