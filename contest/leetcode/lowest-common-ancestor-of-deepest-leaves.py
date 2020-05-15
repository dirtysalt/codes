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
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def find(root):
            if root is None:
                return None, 0

            lr, ld = find(root.left)
            rr, rd = find(root.right)
            if ld > rd:
                return lr, ld + 1
            elif rd > ld:
                return rr, rd + 1
            else:
                return root, ld + 1

        ans, _ = find(root)
        return ans
