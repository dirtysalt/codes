#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def f(root):
            if root is None:
                return -(1 << 31), 0

            lp, lh = f(root.left)
            rp, rh = f(root.right)
            h = max(max(lh, rh) + root.val, 0)
            p = max(lp, rp, lh + rh + root.val)
            return p, h

        p, h = f(root)
        return p
