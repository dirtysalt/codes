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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def fx(root):
            """

            :param root:
            :return: diameter of root, and max height of root
            """

            if root is None:
                return 0, 0

            dl, hl = fx(root.left)
            dr, hr = fx(root.right)
            d = max(dl, dr)
            h = max(hl, hr) + 1
            d = max(d, hl + hr + 1)
            return d, h

        if root is None:
            return 0
        d, h = fx(root)
        return d - 1
