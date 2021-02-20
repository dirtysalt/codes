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
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def fx(root, pv):
            pv = 2 * pv + root.val
            if root.left is None and root.right is None:
                return pv

            res = 0
            if root.left is not None:
                res += fx(root.left, pv)
            if root.right is not None:
                res += fx(root.right, pv)
            return res

        pv = 0
        res = fx(root, pv)
        return res
