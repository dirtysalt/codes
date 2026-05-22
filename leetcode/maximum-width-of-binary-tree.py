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
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = {}
        self.ans = 1

        def f(root, d, idx):
            if root is None:
                return

            if d not in left:
                left[d] = idx
            else:
                width = (idx - left[d]) + 1
                self.ans = max(self.ans, width)

            f(root.left, d + 1, 2 * idx)
            f(root.right, d + 1, 2 * idx + 1)

        f(root, 0, 0)
        return self.ans
