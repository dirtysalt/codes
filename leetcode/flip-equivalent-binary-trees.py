#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def eq(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None:
                return False
            if r1.val != r2.val:
                return False

            r1l, r1r = r1.left, r1.right
            r2l, r2r = r2.left, r2.right

            if eq(r1l, r2l) and eq(r1r, r2r):
                return True
            if eq(r1l, r2r) and eq(r1r, r2l):
                return True
            return False

        ans = eq(root1, root2)
        return ans
