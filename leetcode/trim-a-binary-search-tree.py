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
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        def fn(root):
            if root is None:
                return root

            if L <= root.val <= R:
                root.left = fn(root.left)
                root.right = fn(root.right)
                return root

            elif root.val < L:
                return fn(root.right)

            else:
                return fn(root.left)

        res = fn(root)
        return res
